#
# @file callback_graph_calif_cualitativa_alumnado.py
# @brief Este fichero contiene el callback para actualizar el gráfico de calificaciones
#        cualitativas de las asignaturas matriculadas del perfil "Alumno" de la pestaña
#        "Expediente académico personal".
# @version 1.0
# @date 05/05/2024
# @license MIT License
# @author Fabrizzio Daniell Perilli Martín
# @email alu0101138589@ull.edu.es
#

from dash import Input, Output, callback
import plotly.graph_objs as go
import pandas as pd
from data.queries import calif_cualitativa_asignatura
from util import list_to_tuple


@callback(
    Output("graph-bar-evolucion-asignaturas-matriculadas", "figure"),
    Input("selected-alumnado-store", "data"),
    Input("curso-academico", "value"),
    Input("titulacion-alumnado", "value"),
)
def update_graph_alumnado(alumno_id, curso_academico, titulacion):
    """
    Actualiza el gráfico de calificaciones cualitativas de las asignaturas matriculadas
    del perfil "Alumno" de la pestaña "Expediente académico personal".

    Args:
        alumno_id (str): Identificador del alumno.
        curso_academico (list): Lista con los cursos académicos
        titulacion (str): Titulación seleccionada

    Returns:
        go.Figure: Figura con el gráfico
    """

    fig = go.Figure()

    fig.update_layout(
        title={"text": "Calificaciones cualitativas", "x": 0.5},
        barmode="stack",
        xaxis={"title": "Curso académico"},
        yaxis={"title": "Nº Asignaturas matriculadas"},
        showlegend=True,
        legend={"title": "Calificación"},
    )

    if not (alumno_id and curso_academico and titulacion):
        return fig

    try:
        curso_academico = list_to_tuple(curso_academico)
    except Exception as e:
        print("Error:", e)
        return fig

    data = calif_cualitativa_asignatura(alumno_id, curso_academico, titulacion)

    if not data:
        return fig

    df = pd.DataFrame(data, columns=["curso_academico", "calificacion", "cantidad"])
    df_pivot = df.pivot_table(
        index="curso_academico", columns="calificacion", values="cantidad", fill_value=0
    )

    categories = ["No presentado", "Suspenso", "Aprobado", "Notable", "Sobresaliente"]
    for category in categories:
        if category not in df_pivot.columns:
            df_pivot[category] = 0

    df_pivot = df_pivot[categories]
    df_pivot = df_pivot.sort_index()

    color_mapping = {
        "Sobresaliente": "blue",
        "Notable": "green",
        "Aprobado": "orange",
        "Suspenso": "red",
        "No presentado": "gray",
    }

    for category in categories:
        fig.add_trace(
            go.Bar(
                x=df_pivot.index,
                y=df_pivot[category],
                name=category,
                marker_color=color_mapping[category],
                opacity=0.7,
            )
        )

    return fig
