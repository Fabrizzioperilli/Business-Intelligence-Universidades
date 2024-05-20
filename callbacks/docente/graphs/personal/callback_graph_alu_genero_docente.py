from dash import callback, Input, Output
import plotly.graph_objs as go
from data.queries import alumnos_genero_docente
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
    
    data = alumnos_genero_docente(docente_id, asignaturas, curso_academico)
    
    
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
    colores = {'Mujeres': 'red', 'Hombres': 'blue'}
    
    for sexo in sexos:
        fig.add_trace(go.Bar(
            x=cursos,
            y=[datos_procesados[curso][sexo] for curso in cursos],
            name=sexo,
            marker_color=colores[sexo],
            opacity=0.8
        ))
    
    fig.update_layout(
        barmode='stack',
        title={'text': 'Número de alumnos matriculados por género y curso académico', 'x': 0.5},
        xaxis={'title': 'Curso académico'},
        yaxis={'title': 'Nº Alumnos matriculados'},
        legend_title_text='Género'
    )
    
    return fig
