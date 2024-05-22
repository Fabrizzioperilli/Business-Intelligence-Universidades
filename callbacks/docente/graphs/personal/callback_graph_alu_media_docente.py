from dash import callback, Input, Output
import plotly.graph_objs as go
from data.queries import alumnos_nota_media_docente
from utils.utils import list_to_tuple

@callback(
    Output('graph-alumnos-nota-media', 'figure'),
    [Input('asignaturas-docente', 'value')],
    [Input('curso-academico-docente', 'value')],
    [Input('selected-docente-store', 'data')]
)
def update_graph_docente(asignaturas, curso_academico, docente_id):
    
    fig = go.Figure()
    
    fig.update_layout(
        title={'text': 'Nota media por asignatura y curso académico', 'x': 0.5},
        xaxis_title='Curso académico',
        yaxis_title='Nota media',
        xaxis=dict(type='category')  # Ensures the x-axis uses categorical data
    )
    
    if not asignaturas or not curso_academico or not docente_id:
        return fig
    
    try:
        curso_academico = list_to_tuple(curso_academico)
        asignaturas = list_to_tuple(asignaturas)
    except Exception as e:
        return fig
    
    data = alumnos_nota_media_docente(asignaturas, curso_academico)
    
    if not data:
        return fig
    
    curso_academico = [x[0] for x in data]
    asignatura = [x[1] for x in data]
    media_calif = [x[2] for x in data]

    fig.add_trace(go.Bar(
        x=curso_academico,
        y=media_calif,
        name='Nota media',
        marker=dict(color='blue'),
        opacity=0.8
    ))

    return fig

        



