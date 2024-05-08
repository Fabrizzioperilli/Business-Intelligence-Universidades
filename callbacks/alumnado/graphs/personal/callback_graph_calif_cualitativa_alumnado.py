from dash import Input, Output, callback
from data.db_connector import db
import plotly.graph_objs as go

@callback(
    Output('graph-bar-evolucion-asignaturas-matriculadas', 'figure'),
    [Input('selected-alumnado-store', 'data'), Input('curso-academico', 'value')]
)
def update_graph_alumnado(alumno_id, curso_academico):  

    if not alumno_id or not curso_academico:
        return go.Figure()

    if isinstance(curso_academico, str):
        curso_academico = (curso_academico,)
    else:
        curso_academico = tuple(curso_academico)

    query = """
    SELECT curso_aca, calif, COUNT(*) as grade_count
    FROM lineas_actas
    WHERE id = :alumno_id AND curso_aca IN :curso_academico
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

    categories = ['Suspenso', 'Aprobado', 'Notable', 'Sobresaliente']
    all_courses = sorted(set(row[0] for row in data))
    grade_counts = {category: {course: 0 for course in all_courses} for category in categories}
    
    for row in data:
        curso_aca, calif, grade_count = row
        if calif in grade_counts:
            grade_counts[calif][curso_aca] = grade_count

    traces = []
    color_mapping = {'Sobresaliente': 'blue', 'Notable': 'green', 'Aprobado': 'pink', 'Suspenso': 'red'}
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
        title='Evolución de asignaturas matriculadas por curso académico',
        barmode='stack',
        xaxis={'title': 'Curso académico'},
        yaxis={'title': 'Nº Asignaturas matriculadas'},
        showlegend=True,
    )

    return go.Figure(data=traces, layout=layout)