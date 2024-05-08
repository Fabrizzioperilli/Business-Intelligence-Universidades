from dash import Input, Output, callback
import plotly.graph_objs as go
from data.db_connector import db

@callback(
    Output('graph-evolucion-progreso-academico', 'figure'),
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
    SELECT curso_aca, COUNT(*) as aprobadas
    FROM lineas_actas
    WHERE id = :alumno_id AND calif_numerica >= 5 AND curso_aca IN :curso_academico
    GROUP BY curso_aca
    ORDER BY curso_aca;
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

    academic_years = [row[0] for row in data]
    subjects_passed = [row[1] for row in data]


    cumulative_passed = []
    cumulative_total = 0
    for count in subjects_passed:
        cumulative_total += count
        cumulative_passed.append(cumulative_total)

    trace = go.Bar(x=academic_years, y=cumulative_passed, marker_color='blue', opacity=0.7)

    layout = go.Layout(
        title='Evolución del progreso académico',
        xaxis={'title': 'Curso académico'},
        yaxis={'title': 'Nº Asignaturas de superadas (Acumulativo)'},
        showlegend=False,
    )

    figure = go.Figure(data=[trace], layout=layout)
    return figure