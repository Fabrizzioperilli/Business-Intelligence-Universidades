#
# @file callback_graph_nuevo_ingreso_genero_gestor.py
# @brief Este fichero contiene el callback para actualizar el gráfico
#       de alumnos de nuevo ingreso por género y titulación del perfil "Gestor"
#       de la pestaña "Indicadores académicos".
# @version 1.0
# @date 21/05/2024
# @license MIT License
# @author Fabrizzio Daniell Perilli Martín
# @email alu0101138589@ull.edu.es
#

from dash import Input, Output, State, callback
import plotly.graph_objs as go
import dash_bootstrap_components as dbc
import pandas as pd
from util import list_to_tuple
from data.queries import alumnos_nuevo_ingreso_genero_titulacion, universidades_gestor


@callback(
    Output("nuevo-ingreso-genero-gestor", "figure"),
    Input("selected-gestor-store", "data"),
    Input("curso-academico-gestor", "value"),
    Input("titulaciones-gestor", "value"),
)
def update_graph_gestor(gestor_id, curso_academico, titulaciones):
    """ 
    Actualiza el gráfico de alumnos de nuevo ingreso por género y titulación
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
        title={"text": "Alumnos de nuevo ingreso por género y titulación", "x": 0.5},
        xaxis=dict(title="Titulaciones"),
        yaxis=dict(title="Nº Alumnos"),
        showlegend=True,
        legend={"title": "Género"},
    )

    # Asegurarse de que las columnas sean consistentes
    def map_genero(genero):
        if "masculin" in genero.lower():
            return "Hombres"
        elif "fem" in genero.lower():
            return "Mujeres"
        return genero

    df = get_data(gestor_id, curso_academico, titulaciones)

    if df.empty:
        return fig

    df["genero"] = df["genero"].map(map_genero)

    # Pivotear el DataFrame para obtener las cantidades por género en columnas separadas
    df_pivot = df.pivot_table(
        index="titulacion", columns="genero", values="cantidad", aggfunc="sum"
    ).fillna(0)

    # Asegurarse de que las columnas existen antes de graficar
    if "Hombres" in df_pivot.columns:
        fig.add_trace(
            go.Bar(
                x=df_pivot.index,
                y=df_pivot["Hombres"],
                name="Hombres",
                marker_color="blue",
                opacity=0.7,
            )
        )

    if "Mujeres" in df_pivot.columns:
        fig.add_trace(
            go.Bar(
                x=df_pivot.index,
                y=df_pivot["Mujeres"],
                name="Mujeres",
                marker_color="red",
                opacity=0.7,
            )
        )

    return fig


@callback(
    Output("modal-nuevo-ingreso-genero", "is_open"),
    Input("btn-ver-datos-nuevo-ingreso-genero", "n_clicks"),
    State("modal-nuevo-ingreso-genero", "is_open"),
)
def toggle_modal(btn, is_open):
    """
    Alterna la visibilidad del modal que muestra los datos de los alumnos de nuevo ingreso
    
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
    Output("table-container-nuevo-ingreso-genero", "children"),
    Input("btn-ver-datos-nuevo-ingreso-genero", "n_clicks"),
    Input("selected-gestor-store", "data"),
    Input("curso-academico-gestor", "value"),
    Input("titulaciones-gestor", "value"),
)
def update_table(btn, gestor_id, curso_academico, titulaciones):
    """
    Actualiza la tabla de datos de los alumnos de nuevo ingreso por género y titulación
    del perfil "Gestor" de la pestaña "Indicadores académicos".

    Args:
    btn (int): Número de clicks en el botón
    gestor_id (str): ID del gestor seleccionado
    curso_academico (list): Lista con los cursos académicos
    titulaciones (list): Lista con las titulaciones seleccionadas

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
    Output("btn-descargar-nuevo-ingreso-genero", "href"),
    Input("btn-ver-datos-nuevo-ingreso-genero", "n_clicks"),
    State("selected-gestor-store", "data"),
    State("curso-academico-gestor", "value"),
    State("titulaciones-gestor", "value"),
)
def generate_csv(btn, gestor_id, curso_academico, titulaciones):
    """
    Genera un archivo CSV descargable con los datos de los alumnos de nuevo ingres
    por género y titulación del perfil "Gestor" de la pestaña "Indicadores académicos".

    Args:
    btn (int): Número de clicks en el botón
    gestor_id (str): ID del gestor seleccionado
    curso_academico (list): Lista con los cursos académicos
    titulaciones (list): Lista con las titulaciones seleccionadas

    Returns:
    str: Contenido del archivo CSV
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
    Obtiene los datos de la base da datos para el gráfico y tabla

    Args:
    gestor_id (str): ID del gestor seleccionado
    curso_academico (list): Lista con los cursos académicos
    titulaciones (list): Lista con las titulaciones seleccionadas

    Returns:
    pd.DataFrame: Datos para el gráfico y tabla
    """

    empty = pd.DataFrame()

    if not gestor_id or not curso_academico or not titulaciones:
        return empty

    try:
        titulaciones = list_to_tuple(titulaciones)
    except Exception as e:
        return empty, None

    data_universidad = universidades_gestor(gestor_id)
    if not data_universidad:
        return empty

    data = alumnos_nuevo_ingreso_genero_titulacion(
        curso_academico, titulaciones, data_universidad[0][0]
    )

    if not data:
        return empty

    return pd.DataFrame(
        data, columns=["curso_academico", "titulacion", "genero", "cantidad"]
    )
