from dash import callback, Input, Output
import plotly.graph_objs as go
import pandas as pd
from data.queries import asignaturas_superadas_media_abandono, universidad_alumno
from util import list_to_tuple


@callback(
    Output("asignaturas-superadas-general-mi-nota", "figure"),
    Input("curso-academico", "value"),
    Input("selected-alumnado-store", "data"),
    Input("asignaturas-matriculadas", "value"),
    Input("titulacion-alumnado", "value"),
)
def update_graph_alumnado(curso_academico, alumno_id, asignaturas_matriculadas, titulacion):
    """
    Actualiza el gráfico de relación entre la nota media y el número de asignaturas superadas
    por alumno del perfil "Alumno" de la pestaña "Rendimiento académico general".

    Args:
    curso_academico (list): Lista con los cursos académicos
    alumno_id (str): Identificador del alumno
    asignaturas_matriculadas (list): Lista con las asignaturas matriculadas
    titulacion (str): Titulación seleccionada

    Returns:
    go.Figure: Figura con el gráfico
    
    """
    fig = go.Figure()

    fig.update_layout(
        title={
            "text": "Relación nota media y número de asignaturas superadas por alumno",
            "x": 0.5,
        },
        xaxis_title="Nota Media",
        yaxis_title="Nº Asignaturas superadas",
        legend_title="Estado del alumno",
        showlegend=True,
        xaxis=dict(range=[0, 10]),
        yaxis=dict(range=[0, 40]),
    )

    if not (curso_academico and alumno_id and asignaturas_matriculadas and titulacion):
        return fig

    try:
        curso_academico = list_to_tuple(curso_academico)
        asignaturas_matriculadas = list_to_tuple(asignaturas_matriculadas)
    except Exception as e:
        print("Error:", e)
        return fig

    data_universidad = universidad_alumno(alumno_id)

    if not data_universidad:
        return fig

    data = asignaturas_superadas_media_abandono(
        curso_academico, asignaturas_matriculadas, titulacion, data_universidad[0][0]
    )

    if not data:
        return fig

    df = pd.DataFrame(
        data, columns=["Alumno_id", "Abandono", "Nota_Media", "Asignaturas_Superadas"]
    )

    df["Abandono"] = (
        df["Abandono"]
        .str.strip()
        .str.lower()
        .replace({"si": "Abandona", "no": "No abandona"})
    )
    df["Personal"] = df["Alumno_id"].apply(lambda x: " (Yo)" if x == alumno_id else "")
    df["Key"] = df["Abandono"] + df["Personal"]

    colors = {
        "Abandona": "red",
        "No abandona": "blue",
        "Abandona (Yo)": "yellow",
        "No abandona (Yo)": "yellow",
    }

    for key, group in df.groupby("Key"):
        fig.add_trace(
            go.Scatter(
                x=group["Nota_Media"],
                y=group["Asignaturas_Superadas"],
                mode="markers",
                name=key,
                marker=dict(
                    size=12,
                    line=dict(width=2 if " (Yo)" in key else 1),
                    color=colors[key],
                ),
                opacity=1.0 if " (Yo)" in key else 0.8,
            )
        )

    return fig
