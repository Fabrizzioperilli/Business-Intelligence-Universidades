from dash import callback, Input, Output
import plotly.graph_objs as go
import pandas as pd
from data.queries import universidades_gestor, duracion_media_estudios_nota_gestor, cursos_academicos_egresados

@callback(
    Output('duración-estudios-nota-media-gestor', 'figure'),
    Input('selected-gestor-store', 'data'),
    Input('slider-curso-academico-gestor', 'value')
)
def update_graph_gestor(gestor_id, curso_academico):
    fig = go.Figure()

    fig.update_layout(
        title={'text': 'Evolución de la duración de los estudios con respecto a la nota media', 'x': 0.5},
        xaxis_title='Nota media',
        yaxis_title='Duración media de los estudios en años',
        showlegend=True,
        legend_title_text='Ramas del conocimiento',
        xaxis=dict(range=[5, 10], gridcolor='lightgrey'),
        yaxis=dict(range=[0, 10], gridcolor='lightgrey')
    )

    if not gestor_id:
        return fig
    
    data_universidad = universidades_gestor(gestor_id)

    if not data_universidad:
        return fig
    
    data = duracion_media_estudios_nota_gestor(data_universidad)

    if not data:
        return fig
    
    curso_academico_label = {i+1: fecha[0] for i, fecha in enumerate(cursos_academicos_egresados(data_universidad[0][0]))}
    curso_academico = curso_academico_label[curso_academico]
    
       # Convertir los datos a un DataFrame
    df = pd.DataFrame(data, columns=['nota_media', 'titulacion', 'rama', 'curso', 'duracion_media'])

    # Filtrar los datos para el curso académico seleccionado
    df_filtered = df[df['curso'] == curso_academico]

    if df_filtered.empty:
        return fig
    
    # Crear un diccionario para agrupar los datos por 'rama'
    grouped_data = df_filtered.groupby('rama').agg({
        'nota_media': list,
        'duracion_media': list,
        'titulacion': list
    }).reset_index()

    # Añadir las trazas al gráfico
    for _, row in grouped_data.iterrows():
        sizes = [4 * len(t) for t in row['titulacion']]
        text = [
            f'Titulación: {t}<br>Rama: {row["rama"]}<br>Nota Media: {nm} <br>Duración Media: {dm} años'
            for t, nm, dm in zip(row['titulacion'], row['nota_media'], row['duracion_media'])
        ]
        fig.add_trace(go.Scatter(
            x=row['nota_media'],
            y=row['duracion_media'],
            mode='markers',
            marker=dict(
                size=sizes,
                sizemode='area',
                sizeref=2.*max(sizes)/(40.**2),
                sizemin=4
            ),
            name=row['rama'],
            text=text,
            hovertemplate='%{text}<extra></extra>'
        ))

    return fig
