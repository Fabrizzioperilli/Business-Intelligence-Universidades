from dash import Input, Output, callback
import plotly.graph_objs as go
from utils.utils import list_to_tuple
from data.queries import alumnos_nuevo_ingreso_nacionalidad_titulacion, universidades_gestor

@callback(
    Output('nuevo_ingreso_nacionalidad-gestor','figure'),
    Input('selected-gestor-store', 'data'),
    Input('curso-academico-gestor', 'value'),
    Input('titulaciones-gestor', 'value')
)
def update_graph_gestor(docente_id, curso_academico, titulaciones):
    
    fig = go.Figure()
    
    fig.update_layout(
        barmode='stack',
        title='Alumnos de nuevo ingreso por curso académico y nacionalidad',
        xaxis_title='Titulaciones',
        yaxis_title='Nº de alumnos de nuevo ingreso',
        showlegend=True,
        legend_title='Nacionalidad'
    )

    if not docente_id or not curso_academico or not titulaciones:
        return fig
    
    try:
        titulaciones = list_to_tuple(titulaciones)
    except Exception as e:
        return fig
    
    data_universidad = universidades_gestor(docente_id)
    if not data_universidad:
        return fig

    data = alumnos_nuevo_ingreso_nacionalidad_titulacion(data_universidad[0][0], curso_academico, titulaciones)

    if not data:
        return fig

    titulacion_labels = list(set([d[0] for d in data]))
    nacionalidades = list(set([d[1] for d in data]))
    
    
    for nacionalidad in nacionalidades:
        y_values = []
        for titulacion in titulacion_labels:
            y_value = sum(d[2] for d in data if d[0] == titulacion and d[1] == nacionalidad)
            y_values.append(y_value)
        
        fig.add_trace(go.Bar(
            x=titulacion_labels,
            y=y_values,
            name=nacionalidad
        ))

    return fig