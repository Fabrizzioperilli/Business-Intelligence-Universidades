from dash import Input, Output, State, callback
import plotly.graph_objs as go
import dash_bootstrap_components as dbc
import pandas as pd
from utils.utils import list_to_tuple
from data.queries import alumnos_nuevo_ingreso_nacionalidad_titulacion, universidades_gestor

@callback(
    Output('nuevo_ingreso_nacionalidad-gestor','figure'),
    Input('selected-gestor-store', 'data'),
    Input('curso-academico-gestor', 'value'),
    Input('titulaciones-gestor', 'value')
)
def update_graph_gestor(gestor_id, curso_academico, titulaciones):
    fig = go.Figure()
    
    fig.update_layout(
        barmode='stack',
        title={'text':'Alumnos de nuevo ingreso por nacionalidad y titulación','x':0.5},
        xaxis_title='Titulaciones',
        yaxis_title='Nº Alumnos',
        showlegend=True,
        legend={'title':'Nacionalidad'}
    )
    
    df = get_data(gestor_id, curso_academico, titulaciones)

    if df.empty:
        return fig
    
    # Pivotear el DataFrame para obtener las cantidades por nacionalidad en columnas separadas
    df_pivot = df.pivot_table(index='titulacion', columns='nacionalidad', values='cantidad', aggfunc='sum').fillna(0)
    
    for nacionalidad in df_pivot.columns:
        fig.add_trace(
            go.Bar(
                x=df_pivot.index,
                y=df_pivot[nacionalidad],
                name=nacionalidad
            )
        )

    return fig


@callback(
    Output('modal-nuevo-ingreso-nacionalidad', 'is_open'),
    Input('btn-ver-datos-nuevo-ingreso-nacionalidad', 'n_clicks'),
    State('modal-nuevo-ingreso-nacionalidad', 'is_open')
)
def toggle_modal(btn, is_open):
    if btn:
        return not is_open
    return is_open

@callback(
    Output('table-container-nuevo-ingreso-nacionalidad', 'children'),
    Input('btn-ver-datos-nuevo-ingreso-nacionalidad', 'n_clicks'),
    State('selected-gestor-store', 'data'),
    Input('curso-academico-gestor', 'value'),
    Input('titulaciones-gestor', 'value')
)
def update_table(btn, gestor_id, curso_academico, titulaciones):
    if not btn:
        return ""
    
    df = get_data(gestor_id, curso_academico, titulaciones)
    
    if df.empty:
        return dbc.Alert("No hay datos disponibles", color="info")
    
    return dbc.Table.from_dataframe(df.head(50), striped=True, bordered=True, hover=True)

@callback(
    Output('btn-descargar-nuevo-ingreso-nacionalidad', 'href'),
    Input('btn-ver-datos-nuevo-ingreso-nacionalidad', 'n_clicks'),
    State('selected-gestor-store', 'data'),
    Input('curso-academico-gestor', 'value'),
    Input('titulaciones-gestor', 'value')
)
def generate_csv(btn, gestor_id, curso_academico, titulaciones):
    if not btn:
        return ""
    
    df = get_data(gestor_id, curso_academico, titulaciones)

    if df.empty:
        return ""

    csv_string = df.to_csv(index=False, encoding='utf-8')
    csv_string = "data:text/csv;charset=utf-8," + csv_string
    return csv_string



def get_data(gesto_id, curso_academico, titulaciones):
    empty = pd.DataFrame()

    if not gesto_id or not curso_academico or not titulaciones:
        return empty

    data_universidad = universidades_gestor(gesto_id)
    if not data_universidad:
        return empty
    
    try:
        titulaciones = list_to_tuple(titulaciones)
    except Exception as e:
        return empty
    
    data = alumnos_nuevo_ingreso_nacionalidad_titulacion(data_universidad[0][0], curso_academico, titulaciones)

    if not data:
        return empty
    
    return pd.DataFrame(data, columns=['titulacion', 'nacionalidad', 'cantidad'])
