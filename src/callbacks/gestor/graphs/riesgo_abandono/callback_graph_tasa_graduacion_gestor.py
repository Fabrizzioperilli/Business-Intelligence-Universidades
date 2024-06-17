from dash import Input, Output, State, callback
import plotly.graph_objs as go
import dash_bootstrap_components as dbc
import pandas as pd
from util import list_to_tuple
from data.queries import tasa_graduacion_titulacion_gestor, universidades_gestor


@callback(
    Output("tasa-graduacion-gestor", "figure"),
    Input("curso-all-academico-gestor", "value"),
    Input("selected-gestor-store", "data"),
)
def update_graph_gestor(curso_academico, gestor_id):
    """
    Actualiza el gráfico de la tasa de graduación por titulación 
    del perfil "Gestor" de la pestaña "Riesgo de abandono".

    Args:
    curso_academico (list): Lista con los cursos académicos
    gestor_id (str): ID del gestor seleccionado

    Returns:
    go.Figure: Figura con el gráfico
    """

    fig = go.Figure()

    fig.update_layout(
        title={"text": "Tasa de graduación por titulación ", "x": 0.5},
        xaxis_title="Curso académico",
        yaxis_title="Tasa de graduación (%)",
        showlegend=True,
        legend={"title": "Titulaciones", "orientation": "h", "y": -0.5},
    )

    df = get_data(gestor_id, curso_academico)

    if df.empty:
        return fig

    for titulacion, group in df.groupby("titulacion"):
        fig.add_trace(
            go.Scatter(
                x=group["curso_academico"],
                y=group["tasa_graduacion"],
                mode="lines+markers",
                name=titulacion,
            )
        )

    return fig


@callback(
    Output("modal-tasa-graduacion", "is_open"),
    Input("btn-ver-datos-tasa-graduacion", "n_clicks"),
    State("modal-tasa-graduacion", "is_open"),
)
def toggle_modal(btn, is_open):
    """ 
    Alternar la visibilidad del modal de datos de la tasa de graduación por titulación
    del perfil "Gestor" de la pestaña "Riesgo de abandono".

    Args:
    btn (int): Número de clicks en el botón
    is_open (bool): Estado actual del modal
    """

    if btn:
        return not is_open
    return is_open


@callback(
    Output("table-container-tasa-graduacion", "children"),
    Input("btn-ver-datos-tasa-graduacion", "n_clicks"),
    State("curso-all-academico-gestor", "value"),
    State("selected-gestor-store", "data"),
)
def update_table(btn, curso_academico, gestor_id):
    """
    Actualiza la tabla de datos de la tasa de graduación por titulación
    del perfil "Gestor" de la pestaña "Riesgo de abandono".

    Args:
    btn (int): Número de clicks en el botón
    curso_academico (list): Lista con los cursos académicos
    gestor_id (str): ID del gestor seleccionado

    Returns:
    dbc.Table: Tabla con los datos
    """
    if not btn:
        return ""

    df = get_data(gestor_id, curso_academico)

    if df.empty:
        return dbc.Alert("No hay datos disponibles", color="info")

    return dbc.Table.from_dataframe(
        df.head(50), striped=True, bordered=True, hover=True, responsive=True
    )


@callback(
    Output("btn-descargar-tasa-graduacion", "href"),
    Input("btn-ver-datos-tasa-graduacion", "n_clicks"),
    State("curso-all-academico-gestor", "value"),
    State("selected-gestor-store", "data"),
)
def generate_csv(n, curso_academico, gestor_id):
    """
    Genera un archivo CSV descargable con los datos de la tasa de graduación por titulación
    del perfil "Gestor" de la pestaña "Riesgo de abandono".

    Args:
    n (int): Número de clicks en el botón
    curso_academico (list): Lista con los cursos académicos
    gestor_id (str): ID del gestor seleccionado
    """

    if not n:
        return None

    df = get_data(gestor_id, curso_academico)

    if df is None:
        return None

    csv_string = df.to_csv(index=False, encoding="utf-8")
    csv_string = "data:text/csv;charset=utf-8," + csv_string

    return csv_string


def get_data(gestor_id, curso_academico):
    """
    Obtiene los datos de la tasa de graduación por titulación 
    del perfil "Gestor" de la pestaña "Riesgo de abandono".

    Args:
    gestor_id (str): ID del gestor seleccionado
    curso_academico (list): Lista con los cursos académicos

    Returns:
    pd.DataFrame: Datos de la tasa de graduación
    """
    
    empty = pd.DataFrame()

    if not gestor_id or not curso_academico:
        return empty

    try:
        curso_academico = list_to_tuple(curso_academico)
    except Exception as e:
        print("Error:", e)
        return empty

    data_universidad = universidades_gestor(gestor_id)

    if not data_universidad:
        return empty

    data = tasa_graduacion_titulacion_gestor(data_universidad[0][0], curso_academico)

    if not data:
        return empty

    df = pd.DataFrame(
        data,
        columns=[
            "numero_matriculados",
            "numero_egresados",
            "curso_academico",
            "titulacion",
        ],
    )
    df["tasa_graduacion"] = (df["numero_egresados"] / df["numero_matriculados"]) * 100

    return df
