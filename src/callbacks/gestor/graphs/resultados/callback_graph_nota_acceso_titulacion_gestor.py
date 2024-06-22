#
# @file callback_graph_nota_acceso_titulacion_gestor.py
# @brief Este fichero contiene el callback para actualizar el gráfico
#        de evolución de la nota de acceso por titulación
#        del perfil "Gestor" de la pestaña "Resultados académicos".
# @version 1.0
# @date 22/05/2024
# @license MIT License
# @author Fabrizzio Daniell Perilli Martín
# @email alu0101138589@ull.edu.es
#

from dash import Input, Output, State, callback
import plotly.graph_objs as go
import dash_bootstrap_components as dbc
import pandas as pd
from data.queries import nota_media_acceso_titulacion, universidades_gestor


@callback(
    Output("nota-acceso-titulacion", "figure"), 
    Input("selected-gestor-store", "data")
)
def update_grpht_gestor(gestor_id):
    """
    Actualiza el gráfico de evolución de la nota de acceso por titulación
    del perfil "Gestor" de la pestaña "Resultados académicos".

    Args:
        gestor_id (str): ID del gestor seleccionado

    Returns:
        go.Figure: Figura con el gráfico

    """

    fig = go.Figure()

    fig.update_layout(
        title={"text": "Evolución nota de acceso por titulación", "x": 0.5},
        xaxis_title="Curso académico",
        yaxis_title="Nota media de acceso",
        legend={"title": "Titulaciones"},
    )

    df = get_data(gestor_id)

    if df.empty:
        return fig

    for titulation, group in df.groupby("titulacion"):
        fig.add_trace(
            go.Scatter(
                x=group["curso_academico"],
                y=group["nota"],
                mode="lines+markers",
                name=titulation,
            )
        )

    return fig


@callback(
    Output("modal-nota-acceso", "is_open"),
    Input("btn-ver-datos-nota-acceso", "n_clicks"),
    State("modal-nota-acceso", "is_open"),
)
def toggle_modal(btn, is_open):
    """
    Alternar la visibilidad del modal de datos de la nota de acceso por titulación
    del perfil "Gestor" de la pestaña "Resultados académicos".

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
    Output("table-container-nota-acceso", "children"),
    Input("btn-ver-datos-nota-acceso", "n_clicks"),
    State("selected-gestor-store", "data"),
)
def update_table(btn, gestor_id):
    """
    Actualiza la tabla con los datos de la nota de acceso por titulación 
    del perfil "Gestor" de la pestaña "Resultados académicos".

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
    Output("btn-descargar-csv-nota-acceso", "href"),
    Input("btn-ver-datos-nota-acceso", "n_clicks"),
    State("selected-gestor-store", "data"),
)
def generate_csv(btn, gestor_id):
    """
    Genera un archivo CSV con los datos de la nota de acceso por titulación
    del perfil "Gestor" de la pestaña "Resultados académicos".

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
    pd.DataFrame: Datos de la nota de acceso por titulación
    """
    empty = pd.DataFrame()

    if not gestor_id:
        return empty

    data_universidad = universidades_gestor(gestor_id)

    if not data_universidad:
        return empty

    data = nota_media_acceso_titulacion(data_universidad[0][0])

    if not data:
        return empty

    return pd.DataFrame(data, columns=["curso_academico", "titulacion", "nota"])
