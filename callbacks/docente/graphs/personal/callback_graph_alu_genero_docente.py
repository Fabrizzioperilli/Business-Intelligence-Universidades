from dash import callback, Input, Output
import plotly.graph_objs as go
from data.db_connector import db
from utils.utils import list_to_tuple

@callback(
    Output('graph-alumnos-matri-genero', 'figure'),
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
    WITH docente_asignaturas AS (
    SELECT cod_asignatura
    FROM public.docentes
    WHERE id_docente = :docente_id
      AND asignatura = :asignaturas
    ),
    asignaturas_matriculadas AS (
        SELECT DISTINCT am.id, am.cod_asignatura, am.curso_aca
        FROM public.asignaturas_matriculadas am
        JOIN docente_asignaturas da ON am.cod_asignatura = da.cod_asignatura
        WHERE am.curso_aca IN :curso_academico
          AND am.asignatura = :asignaturas
    ),
    estudiantes_sexo AS (
        SELECT DISTINCT m.id AS alumno_id, m.sexo
        FROM public.matricula m
        JOIN asignaturas_matriculadas am ON m.id = am.id
    )
    SELECT am.curso_aca, m.sexo, COUNT(*) AS cantidad
    FROM estudiantes_sexo m
    JOIN asignaturas_matriculadas am ON m.alumno_id = am.id
    GROUP BY am.curso_aca, m.sexo
    ORDER BY am.curso_aca, m.sexo;
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
        return go.Figure()

    # Procesar los datos para el gráfico
    cursos = list(set(row[0] for row in data))
    cursos.sort()
    sexos = ['Mujeres', 'Hombres']
    
    # Inicializar datos procesados
    datos_procesados = {curso: {sexo: 0 for sexo in sexos} for curso in cursos}
    
    for row in data:
        curso = row[0]
        sexo = 'Mujeres' if row[1] == 'Femenino' else 'Hombres'
        datos_procesados[curso][sexo] = row[2]
    
    fig = go.Figure()
    for sexo in sexos:
        fig.add_trace(go.Bar(
            x=cursos,
            y=[datos_procesados[curso][sexo] for curso in cursos],
            name=sexo
        ))
    
    fig.update_layout(
        barmode='stack',
        title={'text': 'Número de alumnos matriculados por género y curso académico', 'x': 0.5},
        xaxis={'title': 'Curso académico'},
        yaxis={'title': 'Nº Alumnos matriculados'},
        legend_title_text='Género'
    )
    
    return fig
