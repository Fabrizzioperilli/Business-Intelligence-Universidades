from dash import callback, Input, Output
import plotly.graph_objs as go
from data.queries import alumnos_nota_media_docente
from utils.utils import list_to_tuple
import pandas as pd

@callback(
    Output('graph-alumnos-nota-media', 'figure'),
    [Input('asignaturas-docente', 'value')],
    [Input('curso-academico-docente', 'value')],
    [Input('selected-docente-store', 'data')]
)
def update_graph_docente(asignaturas, curso_academico, docente_id):
    
    fig = go.Figure()
    
    fig.update_layout(
        title={'text': 'Evolución nota media por asignatura y curso académico', 'x': 0.5},
        xaxis_title='Curso académico',
        yaxis_title='Nota media',
        xaxis=dict(type='category')
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
    
    df = pd.DataFrame(data, columns=['Curso Académico', 'Asignatura', 'Nota Media'])
    
    fig.add_trace(go.Bar(
        x=df['Curso Académico'],
        y=df['Nota Media'],
        name='Nota media',
        marker=dict(color='blue'),
        opacity=0.7
    ))

    return fig

        



