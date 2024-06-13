from dash import callback, Input, Output, State, dcc
import plotly.graph_objs as go
import pandas as pd
import dash_bootstrap_components as dbc
from data.queries import nota_media_acceso_titulacion, universidades_gestor

@callback(
    Output('nota-acceso-titulacion','figure'),
    Input('selected-gestor-store', 'data')
)
def update_grpht_gestor(gestor_id):
    fig = go.Figure()
    
    fig.update_layout(
        title={'text': 'Evolución de nota de acceso por cada titulación', 'x': 0.5},
        xaxis_title='Curso académico',
        yaxis_title='Nota media de acceso',
        showlegend=True,
        legend={'title':'Titulaciones', 'orientation':'h', 'y': -0.5}
    )
    
    df = get_data(gestor_id)

    if df.empty:
        return fig
        
    for titulation, group in df.groupby('titulacion'):
        fig.add_trace(go.Scatter(
            x=group['curso_academico'],
            y=group['nota'],
            mode='lines+markers',
            name=titulation
        ))

    return fig

@callback(
    Output('modal-nota-acceso', 'is_open'),
    Input('btn-ver-datos-nota-acceso', 'n_clicks'),
    State('modal-nota-acceso', 'is_open')
)
def toggle_modal(btn, is_open):
    if btn:
        return not is_open
    return is_open


@callback(
    Output('table-container-nota-acceso', 'children'),
    Input('btn-ver-datos-nota-acceso', 'n_clicks'),
    State('selected-gestor-store', 'data')
)
def update_table(btn, gestor_id):
    if not btn:
        return ""
    
    df = get_data(gestor_id)

    if df.empty:
        return dbc.Alert("No hay datos disponibles", color="info")
    
    return dbc.Table.from_dataframe(df.head(10), striped=True, bordered=True, hover=True)


@callback(
    Output('btn-descargar-csv-nota-acceso', 'href'),
    Input('btn-ver-datos-nota-acceso', 'n_clicks'),
    State('selected-gestor-store', 'data')
)
def generate_csv(btn, gestor_id):
    if not btn:
        return ""
    
    df = get_data(gestor_id)

    if df.empty:
        return ""
    
    csv_string = df.to_csv(index=False, encoding='utf-8')
    csv_string = "data:text/csv;charset=utf-8," + csv_string
    return csv_string


def get_data(gestor_id):
    empty = pd.DataFrame()
    
    if not gestor_id:
        return empty
    
    data_universidad = universidades_gestor(gestor_id)
    
    if not data_universidad:
        return empty
    
    data = nota_media_acceso_titulacion(data_universidad[0][0])

    if not data:
        return empty
    
    return pd.DataFrame(data, columns=['curso_academico', 'titulacion', 'nota'])
