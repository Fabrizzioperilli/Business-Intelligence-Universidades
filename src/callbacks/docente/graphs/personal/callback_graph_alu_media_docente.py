from dash import Input, Output, callback
import plotly.graph_objs as go
import pandas as pd
from data.queries import alumnos_nota_media_docente
from util import list_to_tuple


@callback(
    Output("graph-alumnos-nota-media", "figure"),
    Input("asignaturas-docente", "value"),
    Input("curso-academico-docente", "value"),
    Input("selected-docente-store", "data"),
)
def update_graph_docente(asignaturas, curso_academico, docente_id):
    """
    Actualiza el gráfico de evolución de la nota media por asignatura
    del perfil "Docente" de la pestaña "Rendimiento académico personal".

    Args:
    asignaturas (list): Lista con las asignaturas seleccionadas
    curso_academico (list): Lista con los cursos académicos
    docente_id (str): Identificador del docente

    Returns:
    go.Figure: Figura con el gráfico
    """

    fig = go.Figure()

    fig.update_layout(
        title={"text": "Evolución nota media por asignatura", "x": 0.5},
        xaxis_title="Curso académico",
        yaxis_title="Nota media",
        xaxis=dict(type="category"),
    )

    if not (asignaturas and curso_academico and docente_id):
        return fig

    try:
        curso_academico = list_to_tuple(curso_academico)
        asignaturas = list_to_tuple(asignaturas)
    except Exception as e:
        return fig

    data = alumnos_nota_media_docente(asignaturas, curso_academico)

    if not data:
        return fig

    df = pd.DataFrame(data, columns=["curso_academico", "asignatura", "nota_media"])

    fig.add_trace(
        go.Bar(
            x=df["curso_academico"],
            y=df["nota_media"],
            name="Nota media",
            marker=dict(color="blue"),
            opacity=0.7,
        )
    )

    return fig
