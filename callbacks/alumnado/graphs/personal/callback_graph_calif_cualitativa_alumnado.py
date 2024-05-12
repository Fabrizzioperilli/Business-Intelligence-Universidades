from dash import Input, Output, callback
from data.db_connector import db
import plotly.graph_objs as go
from utils.utils import list_to_tuple

@callback(
    Output('graph-bar-evolucion-asignaturas-matriculadas', 'figure'),
    [Input('selected-alumnado-store', 'data'), Input('curso-academico', 'value')]
)
def update_graph_alumnado(alumno_id, curso_academico):  

    if not alumno_id or not curso_academico:
        return go.Figure()

    try:
        curso_academico = list_to_tuple(curso_academico)
    except Exception as e:
        print("Error:", e)
        return go.Figure()

    # Modificando la consulta para obtener la máxima calificación por curso y por asignatura
    query = """
    WITH RankedGrades AS (
        SELECT curso_aca, calif, ROW_NUMBER() OVER (PARTITION BY curso_aca, asignatura ORDER BY CASE 
            WHEN calif = 'Sobresaliente' THEN 5
            WHEN calif = 'Notable' THEN 4
            WHEN calif = 'Aprobado' THEN 3
            WHEN calif = 'Suspenso' THEN 2
            WHEN calif = 'No presentado' THEN 1
            ELSE 0 END DESC) AS rk
        FROM lineas_actas
        WHERE id = :alumno_id AND curso_aca IN :curso_academico
    )
    SELECT curso_aca, calif, COUNT(*) as grade_count
    FROM RankedGrades
    WHERE rk = 1
    GROUP BY curso_aca, calif
    ORDER BY curso_aca;
    """
    params = {'alumno_id': alumno_id, 'curso_academico': curso_academico}

    try:
        data = db.execute_query(query, params)
    except Exception as e:
        print("Query execution failed:", e)
        return go.Figure()

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
        title={'text': 'Calificación cualitativa de las asignaturas matriculadas del alumno', 'x': 0.5},
        barmode='stack',
        xaxis={'title': 'Curso académico'},
        yaxis={'title': 'Nº Asignaturas matriculadas'},
        showlegend=True,
        legend={'title': 'Calificación'}
    )

    return go.Figure(data=traces, layout=layout)
