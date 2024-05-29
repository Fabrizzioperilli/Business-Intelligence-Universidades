from dash import callback, Input, Output, State
import plotly.graph_objs as go
import dash_bootstrap_components as dbc
import pandas as pd
from data.queries import universidades_gestor, duracion_media_estudios_nota_gestor, cursos_academicos_egresados

# Función para actualizar el gráfico
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
    
    data, _ = get_data(gestor_id, curso_academico)

    if data is None:
        return fig

    df = pd.DataFrame(data, columns=['nota_media', 'titulacion', 'rama', 'curso', 'duracion_media'])

    if df.empty:
        return fig
    
    grouped_data = df.groupby('rama').agg({
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

# Función para saber si se ha pulsado el botón de ver datos
@callback(
    Output('modal-1', 'is_open'),
    Input('btn-ver-datos-1', 'n_clicks'),
    State('modal-1', 'is_open')
)
def toggle_modal(n1, is_open):
    if n1:
        return not is_open
    return is_open

#Función para actualizar la tabla
@callback(
    Output('table-container-1', 'children'),
    Input('btn-ver-datos-1', 'n_clicks'),
    State('selected-gestor-store', 'data'),
    State('slider-curso-academico-gestor', 'value')
)
def update_table(n1, gestor_id, curso_academico):
    if n1:
        data, _ = get_data(gestor_id, curso_academico)
        df = pd.DataFrame(data)
        return dbc.Table.from_dataframe(df.head(30), striped=True, bordered=True, hover=True)
    return ""


# Función para descargar el csv
@callback(
    Output('btn-descargar-csv-1', 'href'),
    Input('btn-ver-datos-1', 'n_clicks'),
    State('selected-gestor-store', 'data'),
    State('slider-curso-academico-gestor', 'value')
)
def generate_csv(n1, gestor_id, curso_academico):
    if n1:
        data, _ = get_data(gestor_id, curso_academico)
        df = pd.DataFrame(data)
        csv_string = df.to_csv(index=False, encoding='utf-8')
        csv_string = "data:text/csv;charset=utf-8," + csv_string
        return csv_string
    return ""


# Función para obtener los datos
def get_data(gestor_id, curso_academico):
    if not gestor_id:
        return None, None
    
    data_universidad = universidades_gestor(gestor_id)
    
    if not data_universidad:
        return None, None
    
    curso_academico_label = {i+1: fecha[0] for i, fecha in enumerate(cursos_academicos_egresados(data_universidad[0][0]))}
    curso_academico = curso_academico_label[curso_academico]

    if not curso_academico:
        return None, None
    
    data = duracion_media_estudios_nota_gestor(data_universidad[0][0], curso_academico)

    if not data:
        return None, None
    
    return data, data_universidad[0][0]