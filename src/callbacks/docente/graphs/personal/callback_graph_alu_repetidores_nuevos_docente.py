from dash import callback, Input, Output
import plotly.graph_objs as go
import pandas as pd
from data.queries import alumnos_repetidores_nuevos
from util import list_to_tuple

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
        title={'text': 'Evolución alumnos de nuevo ingreso y repetidores', 'x': 0.5},
        xaxis={'title': 'Curso académico'},
        yaxis={'title': 'Nº Alumnos matriculados'},
        showlegend=True,
        legend={'orientation': 'h', 'x': 0, 'y': 1.1}
    )

    if not (asignaturas and curso_academico and docente_id):
        return fig
    
    try:
        curso_academico = list_to_tuple(curso_academico)
    except Exception as e:
        return fig
    
    data = alumnos_repetidores_nuevos(docente_id, curso_academico, asignaturas)
    
    if not data:
        return fig
    
    df = pd.DataFrame(data, columns=['curso_academico', 'alumnos_repetidores', 'alumnos_nuevo_ingreso'])

    fig.add_trace(go.Bar(
        x=df['curso_academico'],
        y=df['alumnos_repetidores'],
        name='Alumnos repetidores',
        marker_color='red',
        opacity=0.7
    ))
    
    fig.add_trace(go.Bar(
        x=df['curso_academico'],
        y=df['alumnos_nuevo_ingreso'],
        name='Alumnos de primera matrícula',
        marker_color='green',
        opacity=0.7
    ))
    
    return fig