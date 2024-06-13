from dash import Input, Output, callback
import plotly.graph_objs as go
import pandas as pd
from data.queries import asignaturas_matriculadas_y_superadas
from utils.utils import list_to_tuple

@callback(
    Output('graph-bar-tasa-rendimiento', 'figure'),
    Input('selected-alumnado-store', 'data'), 
    Input('curso-academico', 'value'),
    Input('titulacion-alumnado','value')
)
def update_graph_alumnado(alumno_id, curso_academico, titulacion):

    fig = go.Figure()
    
    fig.update_layout(
        title={'text': 'Tasa de rendimiento por curso académico', 'x': 0.5},
        xaxis={'title': 'Tasa de rendimiento (%)'},
        yaxis={'title': 'Curso académico'},
        showlegend=False,
    )

    if not (alumno_id and curso_academico and titulacion):
        return fig
    
    try:
        curso_academico = list_to_tuple(curso_academico)
    except Exception as e:
        print("Error:", e)
        return fig

    data = asignaturas_matriculadas_y_superadas(alumno_id, curso_academico, titulacion)
   
    if not data:
        return fig

    df = pd.DataFrame(data, columns=['Curso_academico', 'Matriculadas', 'Superadas'])
    df['Tasa_rendimiento'] = (df['Superadas'] / df['Matriculadas']) * 100

    fig.add_trace(go.Bar(
        x=df['Tasa_rendimiento'],
        y=df['Curso_academico'],
        orientation='h',
        marker_color='blue',
        opacity=0.7,
        width=0.7
    ))

    return fig
