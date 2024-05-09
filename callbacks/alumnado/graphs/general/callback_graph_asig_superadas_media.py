from dash import callback, Input, Output
from data.db_connector import db
import plotly.graph_objs as go

@callback(
    Output('asignaturas-superadas-general-mi-nota', 'figure'),
    Input('curso-academico', 'value'),
    Input('selected-alumnado-store', 'data'),  # Asegúrate de que esto envía el ID del alumno actual
    Input('asignaturas-matriculadas', 'value'),
)
def update_graph_alumnado(curso_academico, alumno_id, asignaturas_matriculadas):
    if not curso_academico or not alumno_id or not asignaturas_matriculadas:
        print("Missing inputs.")
        return go.Figure()

    curso_academico = tuple([curso_academico]) if isinstance(curso_academico, str) else tuple(curso_academico)
    asignaturas_matriculadas = tuple([asignaturas_matriculadas]) if isinstance(asignaturas_matriculadas, str) else tuple(asignaturas_matriculadas)

    query = """
    SELECT a.id, a.abandona, AVG(la.max_calif) AS NotaMedia, COUNT(*) AS AsignaturasSuperadas
    FROM 
        (SELECT 
          la.id, 
          la.asignatura,
          MAX(la.calif_numerica) AS max_calif
        FROM 
        lineas_actas la
        WHERE 
          la.curso_aca IN :curso_academico
          AND la.asignatura IN :asignaturas_matriculadas
        GROUP BY 
          la.id, la.asignatura
    ) la
    JOIN alumnos a ON a.id = la.id 
    GROUP BY a.id  
    ORDER BY a.id;
    """

    params = {
        'curso_academico': curso_academico,
        'asignaturas_matriculadas': asignaturas_matriculadas
    }

    try:
        data = db.execute_query(query, params)
    except Exception as e:
        print("Query execution failed:", e)
        return go.Figure()

    if not data:
        print("No data retrieved.")
        return go.Figure()

    fig = go.Figure()

    # Adding scatter plots for each category
    for student in data:
        if student[0] == alumno_id:
            student_status = 'Yo'
        elif student[1] == 1:
            student_status = 'Abandono'
        else:
            student_status = 'No Abandono'
        
        fig.add_trace(
            go.Scatter(
                x=[student[2]], 
                y=[student[3]], 
                mode='markers', 
                name=student_status,
                marker=dict(
                    size=12,
                    line=dict(width=1),
                    color={'Yo': 'yellow', 'Abandono': 'red', 'No Abandono': 'blue'}[student_status]
                ),
                opacity=0.8
            )
        )

    fig.update_layout(
        title='Relación nota media y número de asignaturas superadas por curso académico',
        xaxis_title='Nota Media',
        yaxis_title='Número de asignaturas superadas',
        legend_title='Estado del alumno',
        showlegend=True,
        xaxis=dict(range=[0, 10]),
        yaxis=dict(range=[0, 40])
    )

    return fig
