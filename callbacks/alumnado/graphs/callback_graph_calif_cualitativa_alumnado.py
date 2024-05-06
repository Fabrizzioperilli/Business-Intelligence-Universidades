from dash import Input, Output, callback
from data.db_connector import db
import plotly.graph_objs as go

@callback(
    Output('graph-bar-evolucion-asignaturas-matriculadas', 'figure'),
    [Input('selected-alumnado-store', 'data'), Input('curso-academico', 'value')]
)
def update_graph_alumnado(alumno_id, curso_academico):
    # Ensure curso_academico is a tuple
    if isinstance(curso_academico, str):
        curso_academico = (curso_academico,)
    elif isinstance(curso_academico, list):
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
        data = []

    if not data:
        print("No data returned from the query.")
        return go.Figure()

    # Initialize grade data for all expected types, avoiding KeyErrors
    grade_data = {
        'Sobresaliente': {},
        'Notable': {},
        'Aprobado': {},
        'Suspenso': {}
    }

    # Populate the grade data dictionary
    for row in data:
        curso_aca = row[0]
        calif = row[1]

        # Ensure the grade type exists in `grade_data`
        if calif not in grade_data:
            grade_data[calif] = {}

        # Ensure the academic course exists within the grade type
        if curso_aca not in grade_data[calif]:
            grade_data[calif][curso_aca] = 0

        # Increment the count for this grade type and course
        grade_data[calif][curso_aca] += row[2]

    # Prepare unique list of course years
    all_courses = sorted(set(row[0] for row in data))

    # Retrieve counts using `.get()` to avoid missing key errors
    sobresalientes = [grade_data['Sobresaliente'].get(curso, 0) for curso in all_courses]
    notables = [grade_data['Notable'].get(curso, 0) for curso in all_courses]
    aprobados = [grade_data['Aprobado'].get(curso, 0) for curso in all_courses]
    suspensos = [grade_data['Suspenso'].get(curso, 0) for curso in all_courses]

    # Create bar traces for each grade type
    trace_sobresaliente = go.Bar(x=all_courses, y=sobresalientes, name='Sobresaliente', marker_color='blue', opacity=0.8)
    trace_notable = go.Bar(x=all_courses, y=notables, name='Notable', marker_color='green', opacity=0.8)
    trace_aprobado = go.Bar(x=all_courses, y=aprobados, name='Aprobado', marker_color='pink', opacity=0.8)
    trace_suspenso = go.Bar(x=all_courses, y=suspensos, name='Suspenso', marker_color='red', opacity=0.8)

    layout = go.Layout(
        title='Evolución de asignaturas matriculadas por curso académico',
        barmode='stack',
        xaxis={'title': 'Curso académico'},
        yaxis={'title': 'Nº Asignaturas matriculadas'},
        showlegend=True
    )

    figure = go.Figure(data=[trace_suspenso, trace_aprobado, trace_notable, trace_sobresaliente], layout=layout)
    return figure