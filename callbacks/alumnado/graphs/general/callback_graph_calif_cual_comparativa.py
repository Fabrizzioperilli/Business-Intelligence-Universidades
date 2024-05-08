from dash import callback, Input, Output
from data.db_connector import db
import plotly.graph_objs as go

@callback(
    Output('nota-cualitativa-general-mi-nota', 'figure'),
    Input('curso-academico', 'value'),
    Input('asignaturas-matriculadas', 'value')
)
def update_graph_alumnado(curso_academico, asignaturas_matriculadas):

    if not curso_academico or not asignaturas_matriculadas:
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
    SELECT asignatura, calif, COUNT(*) as grade_count
    FROM lineas_actas
    WHERE asignatura IN :asignaturas_matriculadas AND curso_aca IN :curso_academico
    GROUP BY asignatura, calif
    ORDER BY asignatura;
    """

    params = {'asignaturas_matriculadas': asignaturas_matriculadas, 'curso_academico': curso_academico}

    try:
        data = db.execute_query(query, params)
    except Exception as e:
        print("Query execution failed:", e)
        return go.Figure()
    
    if not data:
        return go.Figure()
    
    categories = ['Suspenso', 'Aprobado', 'Notable', 'Sobresaliente']
    all_subjects = sorted(set(row[0] for row in data))
    grade_counts = {subject: {category: 0 for category in categories} for subject in all_subjects}

    for row in data:
        subject, calif, grade_count = row
        if calif in grade_counts[subject]:
            grade_counts[subject][calif] += grade_count

    traces = []
    color_mapping = {'Sobresaliente': 'blue', 'Notable': 'green', 'Aprobado': 'pink', 'Suspenso': 'red'}

    for subject in all_subjects:
        for category in categories:
            traces.append(
                go.Bar(
                    x=[subject],
                    y=[grade_counts[subject][category]],
                    name=category,
                    marker_color=color_mapping[category],
                    opacity=0.8
                )
            )

    layout = go.Layout(
        title='Alumnos matriculados por asignatura y calificación por curso académico',
        barmode='stack',
        xaxis={'title': 'Asignatura'},
        yaxis={'title': 'Número de Alumnos Matriculados'},
        showlegend=True
    )

    return go.Figure(data=traces, layout=layout)
