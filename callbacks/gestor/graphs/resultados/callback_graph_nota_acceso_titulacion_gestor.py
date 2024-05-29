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
        legend={'title':'Titulaciones'}
    )

    if not gestor_id:
        return fig
    
    data_universidad = universidades_gestor(gestor_id)

    if not data_universidad:
      return fig 
    
    data = nota_media_acceso_titulacion(data_universidad[0][0])
    
    if not data:
      return fig
    
    # Convertir data en un DataFrame
    df = pd.DataFrame(data, columns=['year', 'titulation', 'score'])
    
    # Añadir trazos al gráfico para cada titulación
    for titulation, group in df.groupby('titulation'):
        fig.add_trace(go.Scatter(
            x=group['year'],
            y=group['score'],
            mode='lines+markers',
            name=titulation
        ))

    return fig

@callback(
    Output('modal-2', 'is_open'),
    Input('btn-ver-datos-2', 'n_clicks'),
    State('modal-2', 'is_open')
)
def toggle_modal_2(n2, is_open):
    if n2:
        return not is_open
    return is_open

@callback(
    Output('table-container-2', 'children'),
    Input('btn-ver-datos-2', 'n_clicks'),
    State('selected-gestor-store', 'data')
)
def update_table_2(n2, gestor_id):
    if n2:
        data_universidad = universidades_gestor(gestor_id)
        data = nota_media_acceso_titulacion(data_universidad[0][0])
        df = pd.DataFrame(data)
        return dbc.Table.from_dataframe(df.head(30), striped=True, bordered=True, hover=True)
    return ""

@callback(
    Output('btn-descargar-csv-2', 'href'),
    Input('btn-ver-datos-2', 'n_clicks'),
    State('selected-gestor-store', 'data')
)
def generate_csv_2(n2, gestor_id):
    if n2:
        data_universidad = universidades_gestor(gestor_id)
        data = nota_media_acceso_titulacion(data_universidad[0][0])
        df = pd.DataFrame(data)
        csv_string = df.to_csv(index=False, encoding='utf-8')
        csv_string = "data:text/csv;charset=utf-8," + csv_string
        return csv_string
    return ""
