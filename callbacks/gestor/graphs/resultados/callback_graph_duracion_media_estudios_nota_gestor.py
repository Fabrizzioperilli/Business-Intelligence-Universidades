import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Input, Output, callback
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
    
    fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 1000

    return fig


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
