from dash import Input, Output, callback
import plotly.graph_objs as go
from data.queries import calif_numerica_asignatura
from utils.utils import list_to_tuple

@callback(
    Output('graph-bar-calificaciones-por-asignatura', 'figure'),
    Input('selected-alumnado-store', 'data'), 
    Input('curso-academico', 'value'),
    Input('titulacion-alumnado','value')
)
def update_graph_alumnado(alumno_id, curso_academico, titulacion):
    if not alumno_id or not curso_academico or not titulacion:
        return go.Figure()

    try:
        curso_academico = list_to_tuple(curso_academico)
    except Exception as e:
        return go.Figure()
    
    data = calif_numerica_asignatura(alumno_id, curso_academico, titulacion)

    if not data:
        print("No data returned from the query.")
        return go.Figure()

    subjects = []
    grades = []
    for row in data:
        subject, grade = row
        subjects.append(subject)
        grades.append(grade)

    trace = go.Bar(x=subjects, y=grades, marker_color='blue', opacity=0.7)

    layout = go.Layout(
        title={'text': 'Calificación cuantitativa de las asignaturas matriculadas del alumno', 'x': 0.5},
        xaxis={'title': 'Asignatura', 'tickangle': 45},
        yaxis={'title': 'Calificación'},
        height=600
    )

    figure = go.Figure(data=[trace], layout=layout)
    return figure

