from dash import Output, Input, callback
import plotly.graph_objs as go
import pandas as pd
from data.queries import calif_all_cualitativa_asignaturas
from util import list_to_tuple

@callback(
    Output('calificaiones-cuali-all-asig-docente', 'figure'),
    Input('titulacion-docente', 'value'),
    Input('all-cursos-academicos-docente', 'value'),
    Input('all-asignaturas-titulacion-docente', 'value'),
)
def update_graph_docente(titulacion, curso_academico, asignatura):
    fig = go.Figure()
    
    fig.update_layout(
        barmode='stack',
        title={'text':'Calificaciones cualitativas de la titulación', 'x': 0.5},
        xaxis={'title': 'Asignaturas', 'tickangle': 45},
        yaxis= {'title': 'Nº Alumnos matriculados'},
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

    if not (curso_academico and asignatura):
        return fig
    
    try:
        asignatura = list_to_tuple(asignatura)
    except Exception as e:
        return fig

    data = calif_all_cualitativa_asignaturas(titulacion, curso_academico, asignatura)

    if not data:
        return fig
    
    df = pd.DataFrame(data, columns=['titulacion', 'asignatura', 'calificación', 'n_alumnos'])
    
    colors_mapping = {
        'Sobresaliente': 'blue',
        'Notable': 'green',
        'Aprobado': 'orange',
        'Suspenso': 'red',
        'No presentado': 'gray'
    }

    for calif, color in colors_mapping.items():
        df_calif = df[df['calificación'] == calif]
        fig.add_trace(go.Bar(
            x=df_calif['asignatura'],
            y=df_calif['n_alumnos'],
            name=calif,
            marker_color=color,
            opacity=0.7))
         
    fig.update_xaxes(categoryorder='array', categoryarray=asignatura)    

    return fig
