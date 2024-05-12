from dash import Input, Output, callback
import plotly.graph_objs as go
from data.db_connector import db
from utils.utils import list_to_tuple

@callback(
    Output('graph-bar-calificaciones-por-asignatura', 'figure'),
    [Input('selected-alumnado-store', 'data'), Input('curso-academico', 'value')]
)
def update_graph_alumnado(alumno_id, curso_academico):
    if not alumno_id or not curso_academico:
        return go.Figure()

    try:
        curso_academico = list_to_tuple(curso_academico)
    except Exception as e:
        return go.Figure()  # Cambiado para regresar una figura vacía correctamente

    # Consulta ajustada para seleccionar la máxima calificación por asignatura en los cursos seleccionados
    query = """
    SELECT asignatura, MAX(calif_numerica) as calif_numerica
    FROM lineas_actas
    WHERE id = :alumno_id AND curso_aca IN :curso_academico
    GROUP BY asignatura
    ORDER BY asignatura;
    """
    params = {'alumno_id': alumno_id, 'curso_academico': curso_academico}

    try:
        data = db.execute_query(query, params)
    except Exception as e:
        print("Query execution failed:", e)
        return go.Figure()  # Regresar figura vacía si hay error

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
    )

    figure = go.Figure(data=[trace], layout=layout)
    return figure

