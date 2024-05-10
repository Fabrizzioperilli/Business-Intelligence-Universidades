from dash import Input, Output, callback
import plotly.graph_objs as go
from data.db_connector import db

@callback(
    Output('graph-bar-calificaciones-por-asignatura', 'figure'),
    [Input('selected-alumnado-store', 'data'), Input('curso-academico', 'value')]
)
def update_graph_alumnado(alumno_id, curso_academico):
    if not alumno_id or not curso_academico:
        return go.Figure()

    if isinstance(curso_academico, str):
        curso_academico = (curso_academico,)
    elif isinstance(curso_academico, list):
        curso_academico = tuple(curso_academico)

    # Adjusted query to include sorting by the academic year in descending order
    query = """
    SELECT asignatura, calif_numerica
    FROM lineas_actas
    WHERE id = :alumno_id AND curso_aca IN :curso_academico
    ORDER BY asignatura, curso_aca DESC;
    """
    params = {'alumno_id': alumno_id, 'curso_academico': curso_academico}

    try:
        data = db.execute_query(query, params)
    except Exception as e:
        print("Query execution failed:", e)
        data = []

    if not data:
        print("No data returned from the query.")
        return go.Figure()

    
    subjects = []
    grades = []
    last_subject = None
    for row in data:
        subject, grade = row
        if subject != last_subject:
            subjects.append(subject)
            grades.append(grade)
            last_subject = subject

    trace = go.Bar(x=subjects, y=grades, marker_color='blue', opacity=0.7)


    layout = go.Layout(
        title={'text':'Calificación cuantitativa de las asignaturas matriculadas del alumno', 'x':0.5},
        xaxis={'title': 'Asignatura', 'tickangle': 45},
        yaxis={'title': 'Calificación'},
    )

    figure = go.Figure(data=[trace], layout=layout)
    return figure
