from dash import callback, Output, Input
import plotly.graph_objs as go
import pandas as pd
from data.queries import calif_media_asignaturas
from util import list_to_tuple


@callback(
    Output("calificaiones-media-all-asig-docente", "figure"),
    Input("titulacion-docente", "value"),
    Input("all-cursos-academicos-docente", "value"),
    Input("all-asignaturas-titulacion-docente", "value"),
)
def update_graph_docente(titulacion, curso_academico, asignatura):
    """
    Actualiza el gráfico de nota media por asignatura de la titulación
    seleccionada del perfil "Docente" de la pestaña "Rendimiento académico general".

    Args:
    titulacion (str): Titulación seleccionada
    curso_academico (list): Lista con los cursos académicos
    asignatura (list): Lista con las asignaturas seleccionadas

    Returns:
    go.Figure: Figura con el gráfico
    """

    fig = go.Figure()

    fig.update_layout(
        title={"text": "Nota media por asignatura de la titulación", "x": 0.5},
        xaxis_title="Asignaturas",
        yaxis_title="Nota media",
    )

    if not (curso_academico and asignatura):
        return fig

    try:
        asignatura = list_to_tuple(asignatura)
    except Exception as e:
        return fig

    data = calif_media_asignaturas(titulacion, curso_academico, asignatura)

    if not data:
        return fig

    df = pd.DataFrame(data, columns=["asignatura", "media_calif"])

    fig.add_trace(
        go.Bar(
            x=df["asignatura"], y=df["media_calif"], marker_color="blue", opacity=0.7
        )
    )

    return fig
