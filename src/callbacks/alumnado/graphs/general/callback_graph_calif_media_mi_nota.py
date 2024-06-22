#
# @file callback_graph_calif_media_mi_nota.py
# @brief Este fichero contiene el callback para actualizar el gráfico 
#        de relación calificaciones del alumno con nota media general 
#        del perfil "Alumno" de la pestaña "Rendimiento académico general".
# @version 1.0
# @date 08/05/2024
# @license MIT License
# @author Fabrizzio Daniell Perilli Martín
# @email alu0101138589@ull.edu.es
#

from dash import callback, Input, Output
import pandas as pd
import plotly.graph_objs as go
from data.queries import nota_media_general_mi_nota, universidad_alumno
from util import list_to_tuple


@callback(
    Output("nota-media-general-mi-nota", "figure"),
    Input("curso-academico", "value"),
    Input("asignaturas-matriculadas", "value"),
    Input("selected-alumnado-store", "data"),
    Input("titulacion-alumnado", "value"),
)
def update_graph_alumnado(curso_academico, asignaturas_matriculadas, alumno_id, titulacion):
    """
    Actualiza el gráfico de relación calificaciones del alumno con nota media general
    del perfil "Alumno" de la pestaña "Rendimiento académico general".

    Args:
        curso_academico (list): Lista con los cursos académicos
        asignaturas_matriculadas (list): Lista con las asignaturas matriculadas
        alumno_id (str): Identificador del alumno
        titulacion (str): Titulación seleccionada

    Returns:
        go.Figure: Figura con el gráfico
        
    """
    fig = go.Figure()

    fig.update_layout(
        title={
            "text": "Relación calificaciones del alumno con nota media general",
            "x": 0.5,
        },
        xaxis={"title": "Asignatura", "tickangle": 45},
        yaxis={"title": "Nota"},
        barmode="group",
        height=600,
    )

    if not (curso_academico and asignaturas_matriculadas and alumno_id and titulacion):
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

    data = nota_media_general_mi_nota(
        curso_academico,
        asignaturas_matriculadas,
        alumno_id,
        titulacion,
        data_universidad[0][0],
    )

    if not data:
        return fig

    df = pd.DataFrame(data, columns=["Asignatura", "NotaMediaGeneral", "MiNota"])

    fig.add_trace(
        go.Bar(
            x=df["Asignatura"],
            y=df["MiNota"],
            name="Mi nota",
            marker_color="blue",
            opacity=0.7,
        )
    )

    fig.add_trace(
        go.Bar(
            x=df["Asignatura"],
            y=df["NotaMediaGeneral"],
            name="Nota media general",
            marker_color="grey",
            opacity=0.7,
        )
    )

    return fig
