from dash import callback, Output, Input
import plotly.graph_objs as go
from data.queries import calif_media_asignaturas
from utils.utils import list_to_tuple
import pandas as pd

@callback(
    Output('calificaiones-media-all-asig-docente', 'figure'),
    Input('titulacion-docente', 'value'),
    Input('all-cursos-academicos-docente', 'value'),
    Input('all-asignaturas-titulacion-docente', 'value'),
)
def update_graph_docente(titulacion, curso_academico, asignatura):

    fig = go.Figure()

    fig.update_layout(
        title={'text':'Nota media por titulación, asignaturas y curso académico', 'x': 0.5},
        xaxis_title='Asignaturas',
        yaxis_title='Nota media'
    )

    if not curso_academico or not asignatura:
        return fig

    try:
        asignatura = list_to_tuple(asignatura)
    except Exception as e:
        return fig
    
    data = calif_media_asignaturas(titulacion, curso_academico, asignatura)

    if not data:
        return fig
    
    df = pd.DataFrame(data, columns=['asignatura', 'media_calif'])

    fig.add_trace(go.Bar(
        x=df['asignatura'],
        y=df['media_calif'],
        marker_color='blue',
        opacity=0.7))
    
    return fig



  
  