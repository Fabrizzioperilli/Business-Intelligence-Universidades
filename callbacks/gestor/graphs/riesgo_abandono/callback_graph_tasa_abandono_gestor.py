from dash import callback, Output, Input, State
import plotly.graph_objs as go
from data.queries import tasa_abandono_titulacion_gestor, universidades_gestor
import pandas as pd
from utils.utils import list_to_tuple

@callback(
    Output('tasa-abandono-gestor', 'figure'),
    Input('curso-all-academico-gestor', 'value'),
    Input('selected-gestor-store', 'data'),
)
def update_graph_gestor(curso_academico, gestor_id):
    fig = go.Figure()

    # Configuración del layout de la gráfica
    fig.update_layout(
        title={'text': 'Tasa de abandono por titulación ', 'x': 0.5},
        xaxis_title='Curso académico',
        yaxis_title='Tasa de abandono (%)',
        showlegend=True,
        legend={'title': 'Titulaciones', 'orientation': 'h', 'y': -0.5}
    )

    if not gestor_id or not curso_academico:
        return fig

    # Obtener datos de la universidad según el gestor_id
    data_universidad = universidades_gestor(gestor_id)

    if not data_universidad:
        return fig
    
    try:
        curso_academico = list_to_tuple(curso_academico)
    except Exception as e:
        print("Error:", e)
        return fig

    data = tasa_abandono_titulacion_gestor(data_universidad[0][0], curso_academico)

    if not data:
        return fig

    df = pd.DataFrame(data, columns=['curso_aca', 'titulacion', 'numero_matriculados', 'numero_abandonos'])
    
    df['tasa_abandono'] = (df['numero_abandonos'] / df['numero_matriculados']) * 100

    for titulacion in df['titulacion'].unique():
        df_titulacion = df[df['titulacion'] == titulacion]
        fig.add_trace(go.Scatter(
            x=df_titulacion['curso_aca'],
            y=df_titulacion['tasa_abandono'],
            mode='lines+markers',
            name=titulacion
        ))

    return fig
    
    