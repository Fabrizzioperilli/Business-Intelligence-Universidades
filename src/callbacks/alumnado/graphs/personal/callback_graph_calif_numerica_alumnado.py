from dash import Input, Output, callback
import plotly.graph_objs as go
import pandas as pd
from data.queries import calif_numerica_asignatura
from util import list_to_tuple, random_color


@callback(
    Output("graph-bar-calificaciones-por-asignatura", "figure"),
    Input("selected-alumnado-store", "data"),
    Input("curso-academico", "value"),
    Input("titulacion-alumnado", "value"),
)
def update_graph_alumnado(alumno_id, curso_academico, titulacion):
    """
    Actualiza el gráfico de calificaciones cuantitativas de las asignaturas matriculadas
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
        title={"text": "Calificaciones cuantitativas", "x": 0.5},
        xaxis={"title": "Asignatura", "tickangle": 45},
        yaxis={"title": "Calificación"},
        height=600,
        showlegend=True,
        legend=dict(
            x=1,
            y=1,
            traceorder="normal",
            font=dict(
                size=10,
            ),
            title="Asignaturas",
        ),
    )

    if not (alumno_id and curso_academico and titulacion):
        return fig

    try:
        curso_academico = list_to_tuple(curso_academico)
    except Exception as e:
        print("Error:", e)
        return fig

    data = calif_numerica_asignatura(alumno_id, curso_academico, titulacion)

    if not data:
        return fig

    df = pd.DataFrame(data, columns=["Asignatura", "Calificacion"])
    colors = random_color(len(df))

    for index, row in df.iterrows():
        fig.add_trace(
            go.Bar(
                x=[row["Asignatura"]],
                y=[row["Calificacion"]],
                name=row["Asignatura"],
                marker_color=colors[index],
                opacity=0.7,
            )
        )

    return fig
