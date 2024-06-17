from dash import Input, Output, callback
import plotly.graph_objs as go
import pandas as pd
from data.queries import alumnos_nota_cualitativa_docente
from util import list_to_tuple


@callback(
    Output("graph-alumnos-nota-cualitativa", "figure"),
    Input("asignaturas-docente", "value"),
    Input("curso-academico-docente", "value"),
    Input("selected-docente-store", "data"),
)
def update_graph_docente(asignaturas, curso_academico, docente_id):
    """
    Actualiza el gráfico de evolución de calificaciones cualitativas
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
        barmode="stack",
        title={"text": "Evolución calificaciones cualitativas", "x": 0.5},
        xaxis={"title": "Curso académico"},
        yaxis={"title": "Nº Alumnos matriculados"},
        legend_title_text="Calificación",
    )

    if not (asignaturas and curso_academico and docente_id):
        return fig

    try:
        curso_academico = list_to_tuple(curso_academico)
        asignaturas = list_to_tuple(asignaturas)
    except Exception as e:
        return fig

    data = alumnos_nota_cualitativa_docente(asignaturas, curso_academico)
    if not data:
        return fig

    df = pd.DataFrame(data, columns=["curso_academico", "calificacion", "n_alumnos"])

    # Pivotear el DataFrame para obtener las cantidades por calificación en columnas separadas
    df_pivot = df.pivot(
        index="curso_academico", columns="calificacion", values="n_alumnos"
    ).fillna(0)
    catagories = ["No presentado", "Suspenso", "Aprobado", "Notable", "Sobresaliente"]

    for calif in catagories:
        if calif not in df_pivot:
            df_pivot[calif] = 0

    df_pivot = df_pivot[catagories]

    colors = {
        "Sobresaliente": "blue",
        "Notable": "green",
        "Aprobado": "orange",
        "Suspenso": "red",
        "No presentado": "gray",
    }

    for calif in catagories:
        fig.add_trace(
            go.Bar(
                x=df_pivot.index,
                y=df_pivot[calif],
                name=calif,
                marker=dict(color=colors[calif]),
                opacity=0.7,
            )
        )

    return fig
