from dash import callback, Input, Output
import plotly.graph_objs as go
from data.queries import alumnos_nota_cualitativa_docente
from utils.utils import list_to_tuple
import pandas as pd

@callback(
    Output('graph-alumnos-nota-cualitativa', 'figure'),
    [Input('asignaturas-docente', 'value')],
    [Input('curso-academico-docente', 'value')],
    [Input('selected-docente-store', 'data')]
)
def update_graph_docente(asignaturas, curso_academico, docente_id):

    fig = go.Figure()
    
    fig.update_layout(
        barmode='stack',
        title={'text': 'Evolución calificaciones por curso académico', 'x': 0.5},
        xaxis={'title': 'Curso académico'},
        yaxis={'title': 'Nº Alumnos matriculados'},
        legend_title_text='Calificación'
    )

    if not asignaturas or not curso_academico or not docente_id:
        return fig
    
    try:
        curso_academico = list_to_tuple(curso_academico)
        asignaturas = list_to_tuple(asignaturas)
    except Exception as e:
        return fig
    
    data = alumnos_nota_cualitativa_docente(asignaturas, curso_academico)
    if not data:
        return fig
    
    df = pd.DataFrame(data, columns=['Curso Académico', 'Calificación', 'Nº Alumnos'])
    
    # Pivotear el DataFrame para obtener las cantidades por calificación en columnas separadas
    df_pivot = df.pivot(index='Curso Académico', columns='Calificación', values='Nº Alumnos').fillna(0)
    
    colors = {
        'No presentado': 'gray',
        'Suspenso': 'red',
        'Aprobado': 'orange',
        'Notable': 'green',
        'Sobresaliente': 'blue'
    }
    
    for calif in df_pivot.columns:
        fig.add_trace(go.Bar(
            x=df_pivot.index,
            y=df_pivot[calif],
            name=calif,
            marker=dict(color=colors[calif]),
            opacity=0.7
        ))
    
    return fig
