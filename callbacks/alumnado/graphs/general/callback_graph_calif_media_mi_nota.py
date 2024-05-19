from dash import callback, Input, Output
from data.db_connector import db
import plotly.graph_objs as go
from utils.utils import list_to_tuple

@callback(
    Output('nota-media-general-mi-nota', 'figure'),
    Input('curso-academico', 'value'),
    Input('asignaturas-matriculadas', 'value'),
    Input('selected-alumnado-store', 'data'),
    Input('titulacion-alumnado', 'value')
)

def update_graph_alumnado(curso_academico, asignaturas_matriculadas, alumno_id, titulacion):
    if not curso_academico or not asignaturas_matriculadas or not alumno_id or not titulacion:
        return go.Figure()

    try:
        curso_academico = list_to_tuple(curso_academico)
        asignaturas_matriculadas = list_to_tuple(asignaturas_matriculadas)
    except Exception as e:
        return [], None


    query = """
    SELECT 
        subquery.asignatura, 
        AVG(subquery.max_calif_numerica) AS media_calif,
        MAX(CASE WHEN subquery.id = :alumno_id THEN subquery.max_calif_numerica ELSE NULL END) AS calif_alumno
    FROM (
        SELECT 
            l.asignatura, 
            l.id,
            l.curso_aca,
            MAX(l.calif_numerica) AS max_calif_numerica
        FROM 
            lineas_actas l
        JOIN 
            matricula m ON l.id = m.id AND l.cod_plan = m.cod_plan
        WHERE 
            l.asignatura IN :asignaturas_matriculadas AND 
            l.curso_aca IN :curso_academico AND 
            m.titulacion = :titulacion
        GROUP BY 
            l.asignatura, 
            l.id,
            l.curso_aca
    ) subquery
    GROUP BY 
        subquery.asignatura
    ORDER BY 
        subquery.asignatura;

    """
    params = {
        'asignaturas_matriculadas': asignaturas_matriculadas, 
        'curso_academico': curso_academico,
        'alumno_id': alumno_id,
        'titulacion': titulacion
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
        title={'text':'Nota media general y mi nota por asignaturas y curso académico', 'x':0.5},
        xaxis={'title': 'Asignatura', 'tickangle': 45},
        yaxis={'title': 'Nota'},
        barmode='group',
        legend={'orientation': 'v'},
        height=600,
    )

    return go.Figure(data=traces, layout=layout)
        
        

