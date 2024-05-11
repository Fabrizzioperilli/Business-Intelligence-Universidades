from dash import callback, Input, Output
from data.db_connector import db
import plotly.graph_objs as go
from utils.utils import list_to_tuple

@callback(
    Output('nota-cualitativa-general-mi-nota', 'figure'),
    Input('curso-academico', 'value'),
    Input('asignaturas-matriculadas', 'value'),
    Input('selected-alumnado-store', 'data'),
)
def update_graph_alumnado(curso_academico, asignaturas_matriculadas, alumno_id):
    if not curso_academico or not asignaturas_matriculadas or not alumno_id:
        return go.Figure()

    try:
        curso_academico = list_to_tuple(curso_academico)
        asignaturas_matriculadas = list_to_tuple(asignaturas_matriculadas)
    except Exception as e:
        return [], None

    general_query = """
    SELECT asignatura, calif, COUNT(*) as grade_count
    FROM lineas_actas
    WHERE asignatura IN :asignaturas_matriculadas AND curso_aca IN :curso_academico
    GROUP BY asignatura, calif
    ORDER BY asignatura;
    """

    student_query = """
    SELECT asignatura, calif
    FROM lineas_actas
    WHERE id = :alumno_id AND asignatura IN :asignaturas_matriculadas AND curso_aca IN :curso_academico;
    """

    params = {
        'asignaturas_matriculadas': asignaturas_matriculadas,
        'curso_academico': curso_academico,
        'alumno_id': alumno_id
    }

    try:
        general_data = db.execute_query(general_query, params)
        student_data = db.execute_query(student_query, params)
    except Exception as e:
        print("Query execution failed:", e)
        return go.Figure()

    if not general_data:
        return go.Figure()

    categories = ['Suspenso', 'Aprobado', 'Notable', 'Sobresaliente']
    student_grades = {row[0]: row[1] for row in student_data}
    all_subjects = sorted(set(row[0] for row in general_data))
    grade_counts = {subject: {category: 0 for category in categories} for subject in all_subjects}

    for row in general_data:
        subject, calif, grade_count = row
        if calif in grade_counts[subject]:
            grade_counts[subject][calif] += grade_count

    traces = []
    color_mapping = {'Sobresaliente': 'blue', 'Notable': 'green', 'Aprobado': 'orange', 'Suspenso': 'red'}

    # Crear trazas normales
    for category in categories:
        x = []
        y = []
        for subject in all_subjects:
            x.append(subject)
            y.append(grade_counts[subject][category] - (1 if category == student_grades.get(subject) else 0))
        traces.append(go.Bar(x=x, y=y, name=category, marker=dict(color=color_mapping[category]), opacity=0.7))

    # Crear trazas para resaltar las barras del alumno
    for category in categories:
        x = []
        y = []
        for subject in all_subjects:
            if category == student_grades.get(subject):
                x.append(subject)
                y.append(1)  # Solo resaltar la barra del estudiante con una cuenta de 1
        if y:  # Solo agregar la traza si hay datos
            traces.append(go.Bar(x=x, y=y, name=category + " (Yo)", marker=dict(color=color_mapping[category], line=dict(color='black', width=2)), opacity=0.9))

    layout = go.Layout(
        title={'text': 'Alumnos matriculados por asignatura y calificación <br> por curso académico', 'x': 0.5},
        barmode='stack',
        xaxis={'title': 'Asignatura', 'tickangle': 45},
        yaxis={'title': 'Número de Alumnos Matriculados'},
        showlegend=True,
        legend={'title': 'Calificación'}
    )

    return go.Figure(data=traces, layout=layout)
