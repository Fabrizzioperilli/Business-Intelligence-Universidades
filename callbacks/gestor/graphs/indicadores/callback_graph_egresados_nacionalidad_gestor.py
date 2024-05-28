from dash import Input, Output, callback
import plotly.graph_objs as go
from utils.utils import list_to_tuple
import pandas as pd
from data.queries import alumnos_egresados_nacionalidad_titulacion, universidades_gestor


@callback(
    Output('egresados-nacionalidad-gestor','figure'),
    Input('selected-gestor-store', 'data'),
    Input('curso-academico-gestor', 'value'),
    Input('titulaciones-gestor', 'value')
)
def update_graph_gestor(gestor_id, curso_academico, titulaciones):

    fig = go.Figure()

    fig.update_layout(
        barmode='stack',
        title={'text': 'Alumnos egresados por nacionalidad y titulación', 'x': 0.5},
        xaxis=dict(title='Titulaciones'),
        yaxis=dict(title='Nº de alumnos egresados'),
        showlegend=True,
        legend=dict(title='Nacionalidad')
    )

    if not gestor_id or not curso_academico or not titulaciones:
        return fig
    
    try:
        titulaciones = list_to_tuple(titulaciones)
    except Exception as e:
        return fig
    
    data_universidad = universidades_gestor(gestor_id)
    if not data_universidad:
        return fig

    data = alumnos_egresados_nacionalidad_titulacion(data_universidad[0][0], curso_academico, titulaciones)

    if not data:
        return fig
    
    df = pd.DataFrame(data, columns=['Titulacion', 'Nacionalidad', 'Cantidad'])
    
    # Pivotear el DataFrame para obtener las cantidades por nacionalidad en columnas separadas
    df_pivot = df.pivot_table(index='Titulacion', columns='Nacionalidad', values='Cantidad', aggfunc='sum').fillna(0)
    
    for nacionalidad in df_pivot.columns:
        fig.add_trace(go.Bar(
            x=df_pivot.index,
            y=df_pivot[nacionalidad],
            name=nacionalidad
        ))

    return fig
