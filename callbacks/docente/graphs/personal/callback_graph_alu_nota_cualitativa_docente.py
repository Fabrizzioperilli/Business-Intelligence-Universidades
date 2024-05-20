from dash import callback, Input, Output
import plotly.graph_objs as go
from data.queries import alumnos_nota_cualitativa_docente
from utils.utils import list_to_tuple

@callback(
    Output('graph-alumnos-nota-cualitativa', 'figure'),
    [Input('asignaturas-docente', 'value')],
    [Input('curso-academico-docente', 'value')],
    [Input('selected-docente-store', 'data')]
)
def update_graph_docente(asignaturas, curso_academico, docente_id):
    if not asignaturas or not curso_academico or not docente_id:
        return go.Figure()
    
    try:
        curso_academico = list_to_tuple(curso_academico)
        asignaturas = list_to_tuple(asignaturas)
    except Exception as e:
        return go.Figure()
    
    data = alumnos_nota_cualitativa_docente(asignaturas, curso_academico)
    
    if not data:
        return go.Figure()
    
    cursos = sorted(list(set([x[0] for x in data])))
    calificaciones = ['No presentado', 'Suspendido', 'Aprobado', 'Notable', 'Sobresaliente']
    
    datos_procesados = {curso: {calif: 0 for calif in calificaciones} for curso in cursos}

    for row in data:
        curso_aca, calif, num_alumnos = row
        datos_procesados[curso_aca][calif] = num_alumnos

    fig = go.Figure()

    colors = {
        'No presentado': 'gray',
        'Suspendido': 'red',
        'Aprobado': 'orange',
        'Notable': 'green',
        'Sobresaliente': 'blue'
    }
  
    for calif in calificaciones:
        fig.add_trace(go.Bar(
            x=cursos,
            y=[datos_procesados[curso][calif] for curso in cursos],
            name=calif,
            marker=dict(color=colors[calif]),
            opacity=0.8
        ))
    
    fig.update_layout(
        barmode='stack',
        title={'text': 'Evolución calificaciones por curso académico', 'x': 0.5},
        xaxis={'title': 'Curso académico'},
        yaxis={'title': 'Nº Alumnos matriculados'},
        legend_title_text='Calificación'
    )
    
    return fig
