from dash import Output, Input, State, callback
import plotly.graph_objs as go
import pandas as pd
import dash_bootstrap_components as dbc
from data.queries import tasa_abandono_titulacion_gestor, universidades_gestor
from util import list_to_tuple

@callback(
    Output('tasa-abandono-gestor', 'figure'),
    Input('curso-all-academico-gestor', 'value'),
    Input('selected-gestor-store', 'data'),
)
def update_graph_gestor(curso_academico, gestor_id):
    fig = go.Figure()

    fig.update_layout(
        title={'text': 'Tasa de abandono por titulación ', 'x': 0.5},
        xaxis_title='Curso académico',
        yaxis_title='Tasa de abandono (%)',
        showlegend=True,
        legend={'title': 'Titulaciones', 'orientation': 'h', 'y': -0.5}
    )

    df = get_data(gestor_id, curso_academico)

    if df.empty:
        return fig
    
    df['tasa_abandono'] = (df['numero_abandonos'] / df['numero_matriculados']) * 100

    for titulacion in df['titulacion'].unique():
        df_titulacion = df[df['titulacion'] == titulacion]
        fig.add_trace(go.Scatter(
            x=df_titulacion['curso_academico'],
            y=df_titulacion['tasa_abandono'],
            mode='lines+markers',
            name=titulacion
        ))

    return fig
    
@callback(
    Output('modal-tasa-abandono', 'is_open'),
    Input('btn-ver-datos-tasa-abandono', 'n_clicks'),
    State('modal-tasa-abandono', 'is_open')
)
def toggle_modal(btn, is_open):
    if btn:
        return not is_open
    return is_open

@callback(
    Output('table-container-tasa-abandono', 'children'),
    Input('btn-ver-datos-tasa-abandono', 'n_clicks'),
    State('selected-gestor-store', 'data'),
    Input('curso-all-academico-gestor', 'value')
)
def update_table(btn, gestor_id, curso_academico):
    if not btn:
        return ""
    
    df = get_data(gestor_id, curso_academico)

    if df.empty:
        return dbc.Alert("No hay datos disponibles", color="info")

    df['tasa_abandono'] = (df['numero_abandonos'] / df['numero_matriculados']) * 100
    return dbc.Table.from_dataframe(df.head(50), striped=True, bordered=True, hover=True, responsive=True)


@callback(
    Output('btn-descargar-tasa-abandono', 'href'),
    Input('btn-ver-datos-tasa-abandono', 'n_clicks'),
    State('selected-gestor-store', 'data'),
    Input('curso-all-academico-gestor', 'value')
)
def generate_csv(btn, gestor_id, curso_academico):
    if not btn:
        return ""
    df = get_data(gestor_id, curso_academico)

    if df.empty:
        return ""

    df['tasa_abandono'] = (df['numero_abandonos'] / df['numero_matriculados']) * 100
    csv_string = df.to_csv(index=False, encoding='utf-8')
    csv_string = "data:text/csv;charset=utf-8," + csv_string
    return csv_string


def get_data(gestor_id, curso_academico):
    empty = pd.DataFrame()

    if not gestor_id or not curso_academico:
        return empty
    
    data_universidad = universidades_gestor(gestor_id)
    if not data_universidad:
        return empty
    try:
        curso_academico = list_to_tuple(curso_academico)
    except Exception as e:
        print("Error:", e)
        return empty

    data = tasa_abandono_titulacion_gestor(data_universidad[0][0], curso_academico)

    if not data:
        return empty

    return pd.DataFrame(data, columns=['curso_academico', 'titulacion', 'numero_matriculados', 'numero_abandonos'])


