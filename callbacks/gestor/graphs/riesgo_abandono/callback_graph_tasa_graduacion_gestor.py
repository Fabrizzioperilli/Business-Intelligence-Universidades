from dash import Input, Output, callback
import plotly.graph_objs as go
from utils.utils import list_to_tuple
from data.queries import tasa_graduacion_titulacion_gestor, universidades_gestor
import pandas as pd

@callback(
    Output('tasa-graduacion-gestor', 'figure'),
    Input('curso-all-academico-gestor', 'value'),
    Input('selected-gestor-store', 'data'),
)
def update_graph_gestor(curso_academico, gestor_id):
    fig = go.Figure()

    # Configuración del layout de la gráfica
    fig.update_layout(
        title={'text': 'Tasa de graduación por titulación ', 'x': 0.5},
        xaxis_title='Curso académico',
        yaxis_title='Tasa de graduación (%)',
        showlegend=True,
        legend={'title': 'Titulaciones', 'orientation': 'h', 'y': -0.5}
    )

    if not gestor_id or not curso_academico:
        return fig
    
    try:
        curso_academico = list_to_tuple(curso_academico)
    except Exception as e:
        print("Error:", e)
        return fig
    
    data_universidad = universidades_gestor(gestor_id)

    if not data_universidad:
        return fig
    
    data = tasa_graduacion_titulacion_gestor(data_universidad[0][0], curso_academico)

    if not data:
        return fig
    
    df = pd.DataFrame(data, columns=['numero_matriculados', 'numero_egresados', 'curso_aca', 'titulacion'])

    df['tasa_graduacion'] = (df['numero_egresados'] / df['numero_matriculados']) * 100

    for titulacion in df['titulacion'].unique():
        df_titulacion = df[df['titulacion'] == titulacion]
        fig.add_trace(go.Scatter(
            x=df_titulacion['curso_aca'],
            y=df_titulacion['tasa_graduacion'],
            mode='lines+markers',
            name=titulacion
        ))
    
    return fig
    
