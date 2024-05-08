from dash import Input, Output, callback
import plotly.graph_objs as go
from data.db_connector import db

@callback(
    Output('graph-bar-tasa-exito', 'figure'),
    [Input('selected-alumnado-store', 'data'), Input('curso-academico', 'value')]
)
def update_graph_alumnado(alumno_id, curso_academico):
    if not alumno_id or not curso_academico:
        return go.Figure()
    
    if isinstance(curso_academico, str):
        curso_academico = (curso_academico,)
    elif isinstance(curso_academico, list):
        curso_academico = tuple(curso_academico)

    # Query to calculate success rate per academic year
    query = """
    SELECT m.curso_aca, COUNT(m.cod_asignatura) AS total_asignaturas,
    SUM(CASE WHEN la.calif IN ('Aprobado', 'Notable', 'Sobresaliente') THEN 1 ELSE 0
        END) AS aprobadas
    FROM asignaturas_matriculadas m LEFT JOIN lineas_actas la
    ON m.cod_asignatura = la.cod_asig AND m.curso_aca = la.curso_aca
    WHERE m.id = :alumno_id AND m.curso_aca IN :curso_academico
    GROUP BY m.curso_aca
    ORDER BY m.curso_aca;
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
    success_rates = [(row[2] / row[1]) * 100 for row in data]

    # Create the horizontal bar chart
    trace = go.Bar(
        x=success_rates,
        y=academic_years,
        orientation='h',
        marker_color='blue',
        opacity=0.7,
        width=0.3

    )

    layout = go.Layout(
        title='Tasa de éxito por curso académico',
        xaxis={'title': 'Porcentaje de éxito'},
        yaxis={'title': 'Curso académico'},
        showlegend=False,
    )

    figure = go.Figure(data=[trace], layout=layout)
    return figure
