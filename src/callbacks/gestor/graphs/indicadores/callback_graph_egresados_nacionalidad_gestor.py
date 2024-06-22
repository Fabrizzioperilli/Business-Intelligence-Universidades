#
# @file callback_graph_egresados_nacionalidad_gestor.py
# @brief Este fichero contiene el callback para actualizar el gráfico
#       de alumnos egresados por nacionalidad y titulación del perfil "Gestor"
#       de la pestaña "Indicadores académicos".
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
from util import list_to_tuple
from data.queries import alumnos_egresados_nacionalidad_titulacion, universidades_gestor


@callback(
    Output("egresados-nacionalidad-gestor", "figure"),
    Input("selected-gestor-store", "data"),
    Input("curso-academico-gestor", "value"),
    Input("titulaciones-gestor", "value"),
)
def update_graph_gestor(gestor_id, curso_academico, titulaciones):
    """
    Actualiza el gráfico de alumnos egresados por nacionalidad y titulación
    del perfil "Gestor" de la pestaña "Indicadores académicos".

    Args:
        gestor_id (str): ID del gestor seleccionado
        curso_academico (list): Lista con los cursos académicos
        titulaciones (list): Lista con las titulaciones seleccionadas

    Returns:
        go.Figure: Figura con el gráfico

    """

    fig = go.Figure()

    fig.update_layout(
        barmode="stack",
        title={"text": "Alumnos egresados por nacionalidad y titulación", "x": 0.5},
        xaxis=dict(title="Titulaciones"),
        yaxis=dict(title="Nº Alumnos"),
        showlegend=True,
        legend={"title": "Nacionalidad"},
    )

    df = get_data(gestor_id, curso_academico, titulaciones)

    if df.empty:
        return fig

    df_pivot = df.pivot_table(
        index="titulacion", columns="nacionalidad", values="cantidad", aggfunc="sum"
    ).fillna(0)

    for nacionalidad in df_pivot.columns:
        fig.add_trace(
            go.Bar(x=df_pivot.index, y=df_pivot[nacionalidad], name=nacionalidad)
        )

    return fig


@callback(
    Output("modal-egresados-nacionalidad", "is_open"),
    Input("btn-ver-datos-egresados-nacionalidad", "n_clicks"),
    State("modal-egresados-nacionalidad", "is_open"),
)
def toggle_modal(btn, is_open):
    """
    Alterna la visibilidad del modal con los datos de alumnos egresados por nacionalidad
    
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
    Output("table-container-egresados-nacionalidad", "children"),
    Input("btn-ver-datos-egresados-nacionalidad", "n_clicks"),
    State("selected-gestor-store", "data"),
    Input("curso-academico-gestor", "value"),
    Input("titulaciones-gestor", "value"),
)
def update_table(btn, gestor_id, curso_academico, titulaciones):
    """
    Actualiza la tabla con los datos de alumnos egresados por nacionalidad y titulación
    del perfil "Gestor" de la pestaña "Indicadores académicos".

    Args:
    btn (int): Número de clicks en el botón
    gestor_id (str): ID del gestor seleccionado
    curso_academico (list): Lista con los cursos académicos

    Returns:
    dbc.Table: Tabla con los datos
    """

    if not btn:
        return ""

    df = get_data(gestor_id, curso_academico, titulaciones)

    if df.empty:
        return dbc.Alert("No hay datos disponibles", color="info")

    return dbc.Table.from_dataframe(
        df.head(50), striped=True, bordered=True, hover=True
    )


@callback(
    Output("btn-descargar-egresados-nacionalidad", "href"),
    Input("btn-ver-datos-egresados-nacionalidad", "n_clicks"),
    State("selected-gestor-store", "data"),
    Input("curso-academico-gestor", "value"),
    Input("titulaciones-gestor", "value"),
)
def generate_csv(btn, gestor_id, curso_academico, titulaciones):
    """
    Genera un archivo CSV descargable con los datos de alumnos egresados por nacionalidad
    y titulación del perfil "Gestor" de la pestaña "Indicadores académicos".

    Args:
    btn (int): Número de clicks en el botón
    gestor_id (str): ID del gestor seleccionado
    curso_academico (list): Lista con los cursos académicos
    titulaciones (list): Lista con las titulaciones seleccionadas

    Returns:
    str: Enlace al archivo CSV
    """

    if not btn:
        return ""

    df = get_data(gestor_id, curso_academico, titulaciones)

    if df.empty:
        return ""

    csv_string = df.to_csv(index=False, encoding="utf-8")
    csv_string = "data:text/csv;charset=utf-8," + csv_string
    return csv_string


def get_data(gestor_id, curso_academico, titulaciones):
    """
    Obtiene los datos de alumnos egresados por nacionalidad y titulación
    del perfil "Gestor" de la pestaña "Indicadores académicos".

    Args:
    gestor_id (str): ID del gestor seleccionado
    curso_academico (list): Lista con los cursos académicos
    titulaciones (list): Lista con las titulaciones seleccionadas

    Returns:
    pd.DataFrame: Datos de la consulta
    """
    
    empty = pd.DataFrame()

    if not gestor_id or not curso_academico or not titulaciones:
        return empty

    data_universidad = universidades_gestor(gestor_id)
    if not data_universidad:
        return empty

    try:
        titulaciones = list_to_tuple(titulaciones)
    except Exception as e:
        return empty

    data = alumnos_egresados_nacionalidad_titulacion(
        data_universidad[0][0], curso_academico, titulaciones
    )

    if not data:
        return empty

    return pd.DataFrame(data, columns=["titulacion", "nacionalidad", "cantidad"])
