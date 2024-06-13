from dash import callback, Input, Output
import plotly.graph_objs as go
from data.queries import alumnos_repetidores_nuevos
from utils.utils import list_to_tuple
import pandas as pd

@callback(
    Output('graph-alumnos-repetidores-nuevos', 'figure'),
    Input('asignaturas-docente', 'value'),
    Input('curso-academico-docente', 'value'),
    Input('selected-docente-store', 'data')
)
def update_graph_docente(asignaturas, curso_academico, docente_id):

    fig = go.Figure()

    fig.update_layout(
        barmode='stack',
        title={'text': 'Evolución alumnos matriculados de nuevo ingreso y repetidores', 'x': 0.5},
        xaxis={'title': 'Curso académico'},
        yaxis={'title': 'Nº Alumnos matriculados'},
        showlegend=True,
        legend={'orientation': 'h', 'x': 0, 'y': 1.1}
    )

    if not asignaturas or not curso_academico or not docente_id:
        return fig
    
    try:
        curso_academico = list_to_tuple(curso_academico)
    except Exception as e:
        return fig
    
    data = alumnos_repetidores_nuevos(docente_id, curso_academico, asignaturas)
    
    if not data:
        return fig
    
    df = pd.DataFrame(data, columns=['Curso Académico', 'Alumnos Repetidores', 'Alumnos Nuevo Ingreso'])

    fig.add_trace(go.Bar(
        x=df['Curso Académico'],
        y=df['Alumnos Repetidores'],
        name='Alumnos repetidores',
        marker_color='red',
        opacity=0.7
    ))
    
    fig.add_trace(go.Bar(
        x=df['Curso Académico'],
        y=df['Alumnos Nuevo Ingreso'],
        name='Alumnos de primera matrícula',
        marker_color='green',
        opacity=0.7
    ))
    
    return fig