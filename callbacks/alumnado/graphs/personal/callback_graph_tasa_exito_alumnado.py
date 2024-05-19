from dash import Input, Output, callback
import plotly.graph_objs as go
from data.db_connector import db
from utils.utils import list_to_tuple

@callback(
    Output('graph-bar-tasa-exito', 'figure'),
    Input('selected-alumnado-store', 'data'), 
    Input('curso-academico', 'value'),
    Input('titulacion-alumnado','value')

)
def update_graph_alumnado(alumno_id, curso_academico, titulacion):
    if not alumno_id or not curso_academico or not titulacion:
        return go.Figure()
    
    try:
        curso_academico = list_to_tuple(curso_academico)
    except Exception as e:
        return [], None

    query = """
    SELECT
        AM.curso_aca AS "curso_academico",
        COUNT(DISTINCT AM.asignatura) AS "Total asignaturas matriculadas",
        COUNT(DISTINCT CASE WHEN LA.calif_numerica >= 5 THEN LA.asignatura ELSE NULL END) AS "Total asignaturas superadas"
    FROM
        asignaturas_matriculadas AM
    LEFT JOIN
        lineas_actas LA ON AM.cod_asignatura = LA.cod_asig AND AM.id = LA.id AND AM.curso_aca = LA.curso_aca
    JOIN
        matricula MA ON AM.id = MA.id AND AM.cod_plan = MA.cod_plan
    WHERE
        AM.id = :alumno_id 
        AND AM.curso_aca IN :curso_academico
        AND MA.titulacion = :titulacion
    GROUP BY
        AM.curso_aca;
    """


    params = {'alumno_id': alumno_id, 'curso_academico': curso_academico, 'titulacion': titulacion}

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
        width=0.7

    )

    layout = go.Layout(
        title={'text': 'Tasa de éxito por curso académico del alumno', 'x': 0.5},
        xaxis={'title': 'Porcentaje de éxito'},
        yaxis={'title': 'Curso académico'},
        showlegend=False,
    )

    figure = go.Figure(data=[trace], layout=layout)
    return figure
