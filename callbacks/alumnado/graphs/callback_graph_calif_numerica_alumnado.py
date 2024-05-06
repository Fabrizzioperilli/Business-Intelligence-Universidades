from dash import Input, Output, callback
import plotly.graph_objs as go
from data.db_connector import db

@callback(
    Output('graph-bar-calificaciones-por-asignatura', 'figure'),
    [Input('selected-alumnado-store', 'data'), Input('curso-academico', 'value')]
)
def update_graph_alumnado(alumno_id, curso_academico):
    if isinstance(curso_academico, str):
        curso_academico = (curso_academico,)
    elif isinstance(curso_academico, list):
        curso_academico = tuple(curso_academico)

    # Query to fetch subject grades for the selected student and academic years
    query = """
    SELECT asignatura, calif_numerica
    FROM lineas_actas
    WHERE id = :alumno_id AND curso_aca IN :curso_academico
    ORDER BY asignatura;
    """

    params = {'alumno_id': alumno_id, 'curso_academico': curso_academico}

    # Execute the query
    try:
        data = db.execute_query(query, params)
    except Exception as e:
        print("Query execution failed:", e)
        data = []

    if not data:
        print("No data returned from the query.")
        return go.Figure()

    # Extract subject names and numeric grades
    subjects = [row[0] for row in data]
    grades = [row[1] for row in data]

    # Create the bar chart with custom color coding
    trace = go.Bar(x=subjects, y=grades, marker_color='blue', opacity=0.7)

    layout = go.Layout(
        title='Calificaciones por asignatura',
        xaxis={'title': 'Asignatura'},
        yaxis={'title': 'Calificación'},
        showlegend=False
    )

    figure = go.Figure(data=[trace], layout=layout)
    return figure
