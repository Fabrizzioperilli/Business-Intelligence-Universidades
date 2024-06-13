import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from dash import Input, Output, callback, State
from data.queries import duracion_media_estudios_nota_gestor, universidades_gestor

@callback(
    Output('duración-estudios-nota-media-gestor', 'figure'),
    Input('selected-gestor-store', 'data')
)
def update_graph_gestor(gestor_id):

    data = get_data(gestor_id)

    if data.empty:
        return go.Figure()
     
    fig = px.scatter(
        data, 
        x='nota_media', 
        y='duracion_media', 
        color='rama', 
        size='numero_alumnos', 
        hover_name='titulacion', 
        animation_frame='curso_academico',
        animation_group='rama',
        category_orders={'rama': sorted(data['rama'].unique())}  # Agrupar colores por ramas
    )
    fig.update_layout(
        title={'text': 'Duración media de los estudios con respecto a la nota media', 'x': 0.5},
        xaxis_title='Nota media',
        yaxis_title='Duración media de los estudios',
        showlegend=True,
        legend={'title': 'Rama'}
    )
    fig.update_traces(
        marker=dict(line=dict(width=1, color='DarkSlateGrey')),
        textposition='top center'  # Ajuste de la posición del texto
    )

    # Ajustar el rango de los ejes para que las burbujas no se corten
    fig.update_xaxes(range=[data['nota_media'].min() - 1, data['nota_media'].max() + 1])
    fig.update_yaxes(range=[data['duracion_media'].min() - 1, data['duracion_media'].max() + 1])
    
    fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 1000

    return fig

@callback(
    Output('modal-duracion-estudios', 'is_open'),
    Input('btn-ver-datos-duracion-estudios', 'n_clicks'),
    State('modal-duracion-estudios', 'is_open')
)
def toggle_modal(btn, is_open):
    if btn:
        return not is_open
    return is_open

@callback(
    Output('table-container-duracion-estudios', 'children'),
    Input('btn-ver-datos-duracion-estudios', 'n_clicks'),
    State('selected-gestor-store', 'data')
)
def update_table(btn, gestor_id):
    if not btn:
        return ""
    
    df = get_data(gestor_id)

    if df.empty:
        return dbc.Alert("No hay datos disponibles", color="info")
    
    return dbc.Table.from_dataframe(df.head(20), striped=True, bordered=True, hover=True)


@callback(
    Output('btn-descargar-csv-duracion-estudios', 'href'),
    Input('btn-descargar-csv-duracion-estudios', 'n_clicks'),
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
    
    data = duracion_media_estudios_nota_gestor(data_universidad[0][0])
    if not data:
        return empty
    
    df = pd.DataFrame(data, columns=['nota_media', 'titulacion', 'rama', 
                                     'curso_academico', 'duracion_media', 'numero_alumnos'])
    return df
