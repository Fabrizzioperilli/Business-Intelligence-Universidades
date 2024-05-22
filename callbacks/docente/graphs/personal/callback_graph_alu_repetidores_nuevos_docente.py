from dash import callback, Input, Output
import plotly.graph_objs as go
from data.queries import alumnos_repetidores_nuevos
from utils.utils import list_to_tuple

@callback(
    Output('graph-alumnos-repetidores-nuevos', 'figure'),
    [Input('asignaturas-docente', 'value')],
    [Input('curso-academico-docente', 'value')],
    [Input('selected-docente-store', 'data')]
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
        print('No data found')
        return fig

    cursos_academicos = [row[0] for row in data]
    alumnos_repetidores = [row[1] for row in data]
    alumnos_nuevo_ingreso = [row[2] for row in data]

    fig.add_trace(go.Bar(
        x=cursos_academicos,
        y=alumnos_repetidores,
        name='Alumnos repetidores',
        marker_color='red',
        opacity=0.8
    ))
    
    fig.add_trace(go.Bar(
        x=cursos_academicos,
        y=alumnos_nuevo_ingreso,
        name='Alumnos de primera matrícula',
        marker_color='green',
        opacity=0.8
    ))
    
    return fig