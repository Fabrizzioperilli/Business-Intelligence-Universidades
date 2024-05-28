from dash import Input, Output, callback
import plotly.graph_objs as go
from utils.utils import list_to_tuple
from data.queries import alumnos_nuevo_ingreso_genero_titulacion, universidades_gestor
import pandas as pd

@callback(
    Output('nuevo-ingreso-genero-gestor', 'figure'),
    Input('selected-gestor-store', 'data'),
    Input('curso-academico-gestor', 'value'),
    Input('titulaciones-gestor', 'value')
)
def update_graph_gestor(gestor_id, curso_academico, titulaciones):

    fig = go.Figure()

    fig.update_layout(
        barmode='stack',
        title={'text': 'Alumnos de nuevo ingreso por género y titulación', 'x': 0.5},
        xaxis=dict(title='Titulaciones'),
        yaxis=dict(title='Nº de alumnos de nuevo ingreso'),
        showlegend=True,
        legend=dict(title='Género')
    )

    if not gestor_id or not curso_academico or not titulaciones:
        return fig
    
    try:
        titulaciones = list_to_tuple(titulaciones)
    except Exception as e:
        return [], None
    
    data_universidad = universidades_gestor(gestor_id)
    if not data_universidad:
        return fig
    
    data = alumnos_nuevo_ingreso_genero_titulacion(curso_academico, titulaciones, data_universidad[0][0])

    if not data:
        return fig
    
    df = pd.DataFrame(data, columns=['Curso Académico', 'Titulacion', 'Género', 'Cantidad'])
    
    # Asegurarse de que las columnas sean consistentes
    def map_genero(genero):
        if 'masculin' in genero.lower():
            return 'Hombres'
        elif 'fem' in genero.lower():
            return 'Mujeres'
        return genero

    df['Género'] = df['Género'].map(map_genero)
    
    # Pivotear el DataFrame para obtener las cantidades por género en columnas separadas
    df_pivot = df.pivot_table(index='Titulacion', columns='Género', values='Cantidad', aggfunc='sum').fillna(0)
    
    # Asegurarse de que las columnas existen antes de graficar
    if 'Hombres' in df_pivot.columns:
        fig.add_trace(go.Bar(
            x=df_pivot.index,
            y=df_pivot['Hombres'],
            name='Hombres',
            marker_color='blue',
            opacity=0.7
        ))

    if 'Mujeres' in df_pivot.columns:
        fig.add_trace(go.Bar(
            x=df_pivot.index,
            y=df_pivot['Mujeres'],
            name='Mujeres',
            marker_color='red',
            opacity=0.7
        ))

    return fig