from dash import callback, Input, Output
from data.queries import calif_cualitativa_comparativa
from data.queries import calif_cualitativa_alumno_asignaturas

import plotly.graph_objs as go
from utils.utils import list_to_tuple

@callback(
    Output('nota-cualitativa-general-mi-nota', 'figure'),
    Input('curso-academico', 'value'),
    Input('asignaturas-matriculadas', 'value'),
    Input('selected-alumnado-store', 'data'),
    Input('titulacion-alumnado', 'value')
)
def update_graph_alumnado(curso_academico, asignaturas_matriculadas, alumno_id, titulacion):
    if not curso_academico or not asignaturas_matriculadas or not alumno_id or not titulacion:
        return go.Figure()

    curso_academico = list_to_tuple(curso_academico)
    asignaturas_matriculadas = list_to_tuple(asignaturas_matriculadas)

    general_data = calif_cualitativa_comparativa(curso_academico, asignaturas_matriculadas, titulacion)
    student_data = calif_cualitativa_alumno_asignaturas(alumno_id, curso_academico, asignaturas_matriculadas, titulacion)

    if not general_data:
        return go.Figure()

    categories = ['Suspenso', 'No presentado', 'Aprobado', 'Notable', 'Sobresaliente']
    student_grades = {row[0]: row[1] for row in student_data}
    all_subjects = sorted(set(row[0] for row in general_data))
    grade_counts = {subject: {category: 0 for category in categories} for subject in all_subjects}

    for row in general_data:
        subject, calif, grade_count = row
        if calif in grade_counts[subject]:
            grade_counts[subject][calif] += grade_count

    traces = []
    color_mapping = {'Sobresaliente': 'blue', 'Notable': 'green', 'Aprobado': 'orange' , 'Suspenso': 'red', 'No presentado': 'gray'}

    for category in categories:
        x = []
        y = []
        for subject in all_subjects:
            x.append(subject)
            y.append(grade_counts[subject][category] - (1 if category == student_grades.get(subject) else 0))
        traces.append(go.Bar(x=x, y=y, name=category, marker=dict(color=color_mapping[category]), opacity=0.7))

    for category in categories:
        x = []
        y = []
        for subject in all_subjects:
            if category == student_grades.get(subject):
                x.append(subject)
                y.append(1)
        if y:
            traces.append(go.Bar(x=x, y=y, name=category + " (Yo)", marker=dict(color=color_mapping[category], line=dict(color='black', width=2)), opacity=0.9))

    layout = go.Layout(
        title={'text': 'Alumnos matriculados por asignatura y calificación por curso académico', 'x': 0.5},
        barmode='stack',
        xaxis={'title': 'Asignatura', 'tickangle': 45},
        yaxis={'title': 'Número de Alumnos Matriculados'},
        showlegend=True,
        legend={'title': 'Calificación'},
        height=600,
    )

    return go.Figure(data=traces, layout=layout)
