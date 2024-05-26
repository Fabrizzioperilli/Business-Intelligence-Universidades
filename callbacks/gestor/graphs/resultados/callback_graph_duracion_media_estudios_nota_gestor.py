from dash import callback, Input, Output
import plotly.graph_objs as go
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
    
    # Filtrar los datos para el curso académico seleccionado
    data_filtered = [d for d in data if d[3] == curso_academico]

    if not data_filtered:
        return fig
    
    # Crear un diccionario para agrupar los datos por 'rama'
    grouped_data = {}
    for row in data_filtered:
        nota_media, titulacion, rama, curso, duracion_media = row
        if rama not in grouped_data:
            grouped_data[rama] = {'x': [], 'y': [], 'size': [], 'text': []}
        grouped_data[rama]['x'].append(nota_media)
        grouped_data[rama]['y'].append(duracion_media)
        grouped_data[rama]['size'].append(4 * len(titulacion))  # Tamaño de la burbuja basado en la longitud del nombre de la titulación
        grouped_data[rama]['text'].append(f'Titulación: {titulacion}<br>Rama: {rama}<br>Nota Media: {nota_media} <br>Duración Media: {duracion_media} años')
    
    # Añadir las trazas al gráfico
    for rama, values in grouped_data.items():
        fig.add_trace(go.Scatter(
            x=values['x'],
            y=values['y'],
            mode='markers',
            marker=dict(size=values['size'], sizemode='area', sizeref=2.*max([max(v['size']) for v in grouped_data.values()])/(40.**2), sizemin=4),
            name=rama,
            text=values['text'],
            hovertemplate='%{text}<extra></extra>'
        ))

    return fig
