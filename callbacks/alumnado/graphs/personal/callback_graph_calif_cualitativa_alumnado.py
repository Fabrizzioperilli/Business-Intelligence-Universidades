from dash import Input, Output, callback
from data.queries import calif_cualitativa_asignatura
import plotly.graph_objs as go
from utils.utils import list_to_tuple

@callback(
    Output('graph-bar-evolucion-asignaturas-matriculadas', 'figure'),
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
        print("Error:", e)
        return go.Figure()

    data = calif_cualitativa_asignatura(alumno_id, curso_academico, titulacion)

    if not data:
        return go.Figure()

    categories = ['No presentado', 'Suspenso', 'Aprobado', 'Notable', 'Sobresaliente']
    all_courses = sorted(set(row[0] for row in data))
    grade_counts = {category: {course: 0 for course in all_courses} for category in categories}
    
    for row in data:
        curso_aca, calif, grade_count = row
        if calif in grade_counts:
            grade_counts[calif][curso_aca] = grade_count

    traces = []
    color_mapping = {'Sobresaliente': 'blue', 'Notable': 'green', 'Aprobado': 'orange', 'Suspenso': 'red', 'No presentado': 'gray'}
    for category in categories:
        traces.append(
            go.Bar(
                x=all_courses,
                y=[grade_counts[category].get(course, 0) for course in all_courses],
                name=category,
                marker_color=color_mapping[category],
                opacity=0.8
            )
        )

    layout = go.Layout(
        title={'text': 'Calificación cualitativa de las asignaturas <br> matriculadas del alumno', 'x': 0.5},
        barmode='stack',
        xaxis={'title': 'Curso académico'},
        yaxis={'title': 'Nº Asignaturas matriculadas'},
        showlegend=True,
        legend={'title': 'Calificación'},
        
    )

    return go.Figure(data=traces, layout=layout)
