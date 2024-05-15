from dash import html, dcc, callback, Input, Output
import plotly.graph_objs as go
from data.db_connector import db
from utils.utils import list_to_tuple

@callback(
    Output('graph-alumnos-repetidores-nuevos', 'figure'),
    [Input('asignaturas-docente', 'value')],
    [Input('curso-academico-docente', 'value')],
    [Input('selected-docente-store', 'data')]
)
def update_graph_docente(asignaturas, curso_academico, docente_id):
    if not asignaturas or not curso_academico or not docente_id:
        return go.Figure()
    
    try:
        curso_academico = list_to_tuple(curso_academico)
    except Exception as e:
        return go.Figure()
    
    query = """
    WITH Asignatura AS (
    SELECT DISTINCT am.id AS student_id, am.curso_aca
    FROM public.asignaturas_matriculadas am
    JOIN public.docentes d ON am.cod_asignatura = d.cod_asignatura
    WHERE d.id_docente = :docente_id
    AND am.asignatura = :asignaturas
    AND am.curso_aca IN :curso_academico
    ),
    repetidores AS (
        SELECT DISTINCT am.id AS student_id, MIN(am.curso_aca) AS primer_curso_aca
        FROM public.asignaturas_matriculadas am
        WHERE am.asignatura = :asignaturas
        GROUP BY am.id
        HAVING COUNT(am.curso_aca) > 1
    ),
    alumnos_categoria AS (
        SELECT 
            am.id,
            am.curso_aca,
            CASE 
                WHEN am.id IN (SELECT student_id FROM repetidores WHERE repetidores.primer_curso_aca <> am.curso_aca) THEN 'repetidor'
                ELSE 'nuevo_ingreso'
            END AS categoria
        FROM public.asignaturas_matriculadas am
        WHERE am.asignatura = :asignaturas
        AND am.curso_aca IN :curso_academico
    )
    SELECT
        am.curso_aca AS curso_academico,
        COUNT(DISTINCT am.id) FILTER (WHERE categoria = 'repetidor') AS alumnos_repetidores,
        COUNT(DISTINCT am.id) FILTER (WHERE categoria = 'nuevo_ingreso') AS alumnos_nuevo_ingreso
    FROM alumnos_categoria am
    GROUP BY am.curso_aca
    ORDER BY am.curso_aca;
    """

    params = {
        'curso_academico': curso_academico,
        'asignaturas': asignaturas,
        'docente_id': docente_id
    }

    try:
        data = db.execute_query(query, params)
    except Exception as e:
        print("Query execution failed:", e)
        return go.Figure()
    
    if not data:
        print('No data found')
        return go.Figure()

    cursos_academicos = [row[0] for row in data]
    alumnos_repetidores = [row[1] for row in data]
    alumnos_nuevo_ingreso = [row[2] for row in data]

    trace1 = go.Bar(
        x=cursos_academicos,
        y=alumnos_repetidores,
        name='Alumnos repetidores',
        marker_color='red',
        opacity=0.8
    )
    
    trace2 = go.Bar(
        x=cursos_academicos,
        y=alumnos_nuevo_ingreso,
        name='Alumnos de primera matrícula',
        marker_color='blue',
        opacity=0.8
    )

    layout = go.Layout(
        barmode='stack',
        title={'text': 'Evolución alumnos matriculados de nuevo ingreso y repetidores', 'x': 0.5},
        xaxis={'title': 'Curso académico'},
        yaxis={'title': 'Nº Alumnos matriculados'},
        showlegend=True,
        legend={'orientation': 'h', 'x': 0, 'y': 1.1}
    )
    
    fig = go.Figure(data=[trace1, trace2], layout=layout)
    return fig