from dash import callback, Input, Output, State, dcc
import plotly.graph_objs as go
import dash_bootstrap_components as dbc
import pandas as pd
from data.queries import universidades_gestor, duracion_media_estudios_nota_gestor, cursos_academicos_egresados

# Función para actualizar el gráfico
@callback(
    Output('duración-estudios-nota-media-gestor', 'figure'),
    Input('selected-gestor-store', 'data'),
    Input('slider-curso-academico-gestor', 'value')
)
def update_graph_gestor(gestor_id, curso_academico):
    fig = go.Figure()

    fig.update_layout(
        title={'text': 'Evolución de la duración de los estudios con respecto a la nota media', 'x': 0.5},
        xaxis_title='Nota media',
        yaxis_title='Duración media de los estudios en años',
        showlegend=True,
        legend_title_text='Ramas del conocimiento',
        xaxis=dict(range=[5, 10], gridcolor='lightgrey'),
        yaxis=dict(range=[0, 10], gridcolor='lightgrey')
    )
    
    df = get_data(gestor_id, curso_academico)

    if df.empty:
        return fig
    
    grouped_data = df.groupby('rama').agg({
        'nota_media': list,
        'duracion_media': list,
        'titulacion': list
    }).reset_index()

    # Añadir las trazas al gráfico
    for _, row in grouped_data.iterrows():
        sizes = [4 * len(t) for t in row['titulacion']]
        text = [
            f'Titulación: {t}<br>Rama: {row["rama"]}<br>Nota Media: {nm} <br>Duración Media: {dm} años'
            for t, nm, dm in zip(row['titulacion'], row['nota_media'], row['duracion_media'])
        ]
        fig.add_trace(go.Scatter(
            x=row['nota_media'],
            y=row['duracion_media'],
            mode='markers',
            marker=dict(
                size=sizes,
                sizemode='area',
                sizeref=2.*max(sizes)/(40.**2),
                sizemin=4
            ),
            name=row['rama'],
            text=text,
            hovertemplate='%{text}<extra></extra>'
        ))
    return fig

# Función para saber si se ha pulsado el botón de ver datos
@callback(
    Output('modal-duracion-media', 'is_open'),
    Input('btn-ver-datos-duracion-media', 'n_clicks'),
    State('modal-duracion-media', 'is_open')
)
def toggle_modal(btn, is_open):
    if btn:
        return not is_open
    return is_open

#Función para actualizar la tabla
@callback(
    Output('table-container-duracion-media', 'children'),
    Input('btn-ver-datos-duracion-media', 'n_clicks'),
    State('selected-gestor-store', 'data'),
    State('slider-curso-academico-gestor', 'value')
)
def update_table(btn, gestor_id, curso_academico):
    if not btn:
        return ""
    
    df = get_data(gestor_id, curso_academico)
    if df.empty:
        return dbc.Alert("No hay datos disponibles", color='info')
    
    return dbc.Table.from_dataframe(df.head(10), striped=True, bordered=True, hover=True)


# Función para descargar el csv
@callback(
    Output('btn-descargar-csv-duracion-media', 'href'),
    Input('btn-ver-datos-duracion-media', 'n_clicks'),
    State('selected-gestor-store', 'data'),
    State('slider-curso-academico-gestor', 'value')
)
def generate_csv(btn, gestor_id, curso_academico):
    if not btn:
        return ""
    
    df = get_data(gestor_id, curso_academico)

    if df.empty:
        return ""

    csv_string = df.to_csv(index=False, encoding='utf-8')
    csv_string = "data:text/csv;charset=utf-8," + csv_string
    return csv_string


# Función para obtener los datos
def get_data(gestor_id, curso_academico):
    empty = pd.DataFrame()
    
    if not gestor_id or not curso_academico:
        return empty
    
    data_universidad = universidades_gestor(gestor_id)
    
    if not data_universidad:
        return empty
    
    curso_academico_label = {i+1: fecha[0] for i, fecha in enumerate(cursos_academicos_egresados(data_universidad[0][0]))}
    curso_academico = curso_academico_label[curso_academico]

    if not curso_academico:
        return empty
    
    data = duracion_media_estudios_nota_gestor(data_universidad[0][0], curso_academico)

    if not data:
        return empty
    
    return pd.DataFrame(data, columns=['nota_media', 'titulacion', 'rama', 'curso_academico', 'duracion_media'])