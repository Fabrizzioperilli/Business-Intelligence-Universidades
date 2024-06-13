from dash import callback, Output, Input
import plotly.graph_objs as go
from data.queries import calif_all_cualitativa_asignaturas
from utils.utils import list_to_tuple
import pandas as pd

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
        title={'text':'Calificaciones cualitativas por titulación, asignaturas y curso académico ', 'x': 0.5},
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

    if not curso_academico or not asignatura:
        return fig
    
    try:
        asignatura = list_to_tuple(asignatura)
    except Exception as e:
        return fig
    
    data = calif_all_cualitativa_asignaturas(titulacion, curso_academico, asignatura)

    if not data:
        return fig
    df = pd.DataFrame(data, columns=['Titulacion', 'Asignatura', 'Calificación', 'N_Alumnos'])
    
    colors = {
        'Sobresaliente': 'blue',
        'Notable': 'green',
        'Aprobado': 'orange',
        'Suspenso': 'red',
        'No presentado': 'gray'
    }

    for calif, color in colors.items():
        df_filtered = df[df['Calificación'] == calif]
        if not df_filtered.empty:
            fig.add_trace(go.Bar(
                x=df_filtered['Asignatura'],
                y=df_filtered['N_Alumnos'],
                name=calif,
                marker_color=color,
                opacity=0.7
            ))

    return fig
