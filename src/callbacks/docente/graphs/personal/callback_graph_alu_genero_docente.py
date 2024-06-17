from dash import Input, Output, callback
import plotly.graph_objs as go
import pandas as pd
from data.queries import alumnos_genero_docente
from util import list_to_tuple


@callback(
    Output("graph-alumnos-matri-genero", "figure"),
    Input("asignaturas-docente", "value"),
    Input("curso-academico-docente", "value"),
    Input("selected-docente-store", "data"),
)
def update_graph_docente(asignaturas, curso_academico, docente_id):
    """
    Actualiza el gráfico de evolución de alumnos matriculados por género
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
        title={"text": "Evolución alumnos matriculados por género", "x": 0.5},
        xaxis={"title": "Curso académico"},
        yaxis={"title": "Nº Alumnos matriculados"},
        legend={"title": "Género"},
    )

    if not (asignaturas and curso_academico and docente_id):
        return fig

    try:
        curso_academico = list_to_tuple(curso_academico)
    except Exception as e:
        return fig

    data = alumnos_genero_docente(docente_id, asignaturas, curso_academico)

    if not data:
        return fig

    df = pd.DataFrame(data, columns=["curso_academico", "genero", "cantidad"])

    df_pivot = df.pivot(
        index="curso_academico", columns="genero", values="cantidad"
    ).fillna(0)

    colores = {"Femenino": "red", "Masculino": "blue"}

    for genero in df_pivot.columns:
        fig.add_trace(
            go.Bar(
                x=df_pivot.index,
                y=df_pivot[genero],
                name="Mujeres" if genero == "Femenino" else "Hombres",
                marker_color=colores[genero],
                opacity=0.7,
            )
        )

    return fig
