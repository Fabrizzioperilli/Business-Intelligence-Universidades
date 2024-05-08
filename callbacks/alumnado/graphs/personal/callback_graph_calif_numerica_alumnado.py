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

    query = """
    SELECT asignatura, calif_numerica
    FROM lineas_actas
    WHERE id = :alumno_id AND curso_aca IN :curso_academico
    ORDER BY asignatura;
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

    subjects = [row[0] for row in data]
    grades = [row[1] for row in data]

    trace = go.Bar(x=subjects, y=grades, marker_color='blue', opacity=0.7)

    layout = go.Layout(
        title={'text':'Calificación cuantitativa de las asignaturas matriculadas', 'x':0.5},
        xaxis={'title': 'Asignatura'},
        yaxis={'title': 'Calificación'},
        showlegend=False,
    )

    figure = go.Figure(data=[trace], layout=layout)
    return figure
