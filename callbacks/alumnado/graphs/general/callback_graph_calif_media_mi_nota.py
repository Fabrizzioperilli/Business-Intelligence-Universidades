from dash import callback, Input, Output
from data.db_connector import db
import plotly.graph_objs as go

@callback(
    Output('nota-media-general-mi-nota', 'figure'),
    Input('curso-academico', 'value'),
    Input('asignaturas-matriculadas', 'value'),
    Input('selected-alumnado-store', 'data'),
)

def update_graph_alumnado(curso_academico, asignaturas_matriculadas, alumno_id):
    if not curso_academico or not asignaturas_matriculadas or not alumno_id:
        return go.Figure()

    if isinstance(curso_academico, str):
        curso_academico = (curso_academico,)
    else:
        curso_academico = tuple(curso_academico)

    if isinstance(asignaturas_matriculadas, str):
        asignaturas_matriculadas = (asignaturas_matriculadas,)
    else:
        asignaturas_matriculadas = tuple(asignaturas_matriculadas)

    query = """
    SELECT l.asignatura, AVG(l.calif_numerica) AS media_calif, 
    MAX(CASE WHEN l.id = :alumno_id THEN l.calif_numerica ELSE NULL END) AS calif_alumno  
	FROM lineas_actas l 
    WHERE l.asignatura IN :asignaturas_matriculadas AND l.curso_aca IN :curso_academico
	GROUP BY l.asignatura;
    """
    params = {
        'asignaturas_matriculadas': asignaturas_matriculadas, 
        'curso_academico': curso_academico,
        'alumno_id': alumno_id
    }

    try:
        data = db.execute_query(query, params)
    except Exception as e:
        print("Query execution failed:", e)
        return go.Figure()

    if not data:
        return go.Figure()

    all_subjects = [row[0] for row in data]
    avg_grades = [row[1] for row in data]
    student_grades = [row[2] for row in data]

    traces = [
        go.Bar(
            x=all_subjects,
            y=student_grades,
            name='Mi nota',
            marker_color='blue',
            opacity=0.8,
        ),
        go.Bar(
            x=all_subjects,
            y=avg_grades,
            name='Nota media general',
            marker_color='grey',
            opacity=0.8
        )
    ]

    layout = go.Layout(
        title={'text':'Nota media general y mi nota por asignaturas y curso <br> académico', 'x':0.5},
        xaxis={'title': 'Asignatura'},
        yaxis={'title': 'Nota'},
        barmode='group',
        legend={'orientation': 'v'}
    )

    return go.Figure(data=traces, layout=layout)
        
        

