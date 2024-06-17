from dash import Input, Output, State, callback
import plotly.express as px
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
import pandas as pd
from data.queries import duracion_media_estudios_nota_gestor, universidades_gestor


@callback(
    Output("duración-estudios-nota-media-gestor", "figure"),
    Input("selected-gestor-store", "data"),
)
def update_graph_gestor(gestor_id):
    """
    Actualiza el gráfico de duración media de los estudios con respecto a la nota media
    del perfil "Gestor" de la pestaña "Resultados académicos".

    Args:
    gestor_id (str): ID del gestor seleccionado

    Returns:
    go.Figure: Figura con el gráfico
    """

    fig = go.Figure()

    if not gestor_id:
        return fig

    data = get_data(gestor_id)

    if data.empty:
        return fig

    fig = px.scatter(
        data,
        x="nota_media",
        y="duracion_media",
        color="rama",
        size="numero_alumnos",
        hover_name="titulacion",
        animation_frame="curso_academico",
        animation_group="rama",
        category_orders={
            "rama": sorted(data["rama"].unique())
        },
    )

    fig.update_layout(
        title={
            "text": "Duración media de los estudios con respecto a la nota media",
            "x": 0.5,
        },
        xaxis_title="Nota media",
        yaxis_title="Duración media de los estudios",
        legend={"title": "Rama de conocimiento"},
    )

    fig.update_traces(
        marker=dict(line=dict(width=1, color="DarkSlateGrey")),
        textposition="top center"
    )

    # Ajustar el rango de los ejes para que las burbujas no se corten
    fig.update_xaxes(range=[data["nota_media"].min() - 1, data["nota_media"].max() + 1])
    fig.update_yaxes(
        range=[data["duracion_media"].min() - 1, data["duracion_media"].max() + 1]
    )

    fig.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"] = 1000

    return fig


@callback(
    Output("modal-duracion-estudios", "is_open"),
    Input("btn-ver-datos-duracion-estudios", "n_clicks"),
    State("modal-duracion-estudios", "is_open"),
)
def toggle_modal(btn, is_open):
    """
    Alterna la visibilidad del modal con los datos de duración media de los estudios
    con respecto a la nota media.
    
    Args:
    btn (int): Número de clicks en el botón
    is_open (bool): Estado actual del modal
    
    Returns:
    bool: Nuevo estado del modal
    """
    if btn:
        return not is_open
    return is_open


@callback(
    Output("table-container-duracion-estudios", "children"),
    Input("btn-ver-datos-duracion-estudios", "n_clicks"),
    State("selected-gestor-store", "data"),
)
def update_table(btn, gestor_id):
    """
    Actualiza la tabla con los datos de duración media de los estudios
    con respecto a la nota media del perfil "Gestor" de la pestaña "Resultados académicos".

    Args:
    btn (int): Número de clicks en el botón
    gestor_id (str): ID del gestor seleccionado

    Returns:
    dbc.Table: Tabla con los datos
    """
    if not btn:
        return ""

    df = get_data(gestor_id)

    if df.empty:
        return dbc.Alert("No hay datos disponibles", color="info")

    return dbc.Table.from_dataframe(
        df.head(50), striped=True, bordered=True, hover=True
    )


@callback(
    Output("btn-descargar-csv-duracion-estudios", "href"),
    Input("btn-descargar-csv-duracion-estudios", "n_clicks"),
    State("selected-gestor-store", "data"),
)
def generate_csv(btn, gestor_id):
    """
    Genera un archivo CSV descargable con los datos de duración media de los estudios
    con respecto a la nota media del perfil "Gestor" de la pestaña "Resultados académicos".

    Args:
    btn (int): Número de clicks en el botón
    gestor_id (str): ID del gestor seleccionado

    Returns:
    str: Enlace al archivo CSV
    """

    if not btn:
        return ""

    df = get_data(gestor_id)

    if df.empty:
        return ""

    csv_string = df.to_csv(index=False, encoding="utf-8")
    csv_string = "data:text/csv;charset=utf-8," + csv_string
    return csv_string


def get_data(gestor_id):
    """
    Obtiene los datos de la base de datos.
    
    Args:
    gestor_id (str): ID del gestor seleccionado
    
    Returns:
    pd.DataFrame: Datos de la base de datos
    """
    empty = pd.DataFrame()

    if not gestor_id:
        return empty

    data_universidad = universidades_gestor(gestor_id)
    if not data_universidad:
        return empty

    data = duracion_media_estudios_nota_gestor(data_universidad[0][0])
    if not data:
        return empty

    df = pd.DataFrame(
        data,
        columns=[
            "nota_media",
            "titulacion",
            "rama",
            "curso_academico",
            "duracion_media",
            "numero_alumnos",
        ],
    )
    return df
