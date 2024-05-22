from dash import callback, Output, Input
import plotly.graph_objs as go
from data.queries import calif_all_cualitativa_asignaturas
from utils.utils import list_to_tuple


@callback(
    Output('calificaiones-cuali-all-asig-docente', 'figure'),
    Input('titulacion-docente', 'value'),
    Input('all-cursos-academicos-docente', 'value'),
    Input('all-asignaturas-titulacion-docente', 'value'),
)
def update_graph_all_calif_cualitativa_docente(titulacion, curso_academico, asignatura):

    fig = go.Figure()
    
    fig.update_layout(
        barmode='stack',
        title={'text':'Alumnos matriculados por asignatura y relación con la calificación por curso académico', 'x': 0.5},
        xaxis_title='Asignaturas',
        yaxis_title='Nº Alumnos matriculados',
        height=700,
        legend=dict(
            x=1,
            y=1,
            traceorder='normal',
            font=dict(
                size=10,  # Ajusta el tamaño de la fuente para que sea más pequeño
            ),
            title='Calificaciones'
        )
    )

    if not curso_academico or not asignatura:
        return fig
    
    try:
        asignatura = list_to_tuple(asignatura)
    except Exception as e:
        return fig
    
    data = calif_all_cualitativa_asignaturas(titulacion, curso_academico, asignatura)

    if not data:
        return fig
    
    colors = {
        'Sobresaliente': 'blue',
        'Notable': 'green',
        'Aprobado': 'orange',
        'Suspenso': 'red',
        'No presentado': 'gray'
    }

    
    for calif in colors.keys():
        filtered_data = [d for d in data if d[2] == calif]
        if filtered_data:
            x = [d[1] for d in filtered_data] 
            y = [d[3] for d in filtered_data]
            fig.add_trace(
                go.Bar(
                    x=x,
                    y=y,
                    name=calif,
                    marker_color=colors[calif],
                    opacity=0.8
                )
            )

    return fig
