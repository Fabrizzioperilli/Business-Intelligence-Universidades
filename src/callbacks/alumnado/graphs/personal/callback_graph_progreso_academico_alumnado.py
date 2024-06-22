#
# @file callback_graph_progreso_academico_alumnado.py
# @brief Este fichero contiene el callback para actualizar el gráfico 
#        de evolución del progreso académico del perfil "Alumno" de la 
#        pestaña "Expediente académico personal".
# @version 1.0
# @date 06/05/2024
# @license MIT License
# @author Fabrizzio Daniell Perilli Martín
# @email alu0101138589@ull.edu.es
#

from dash import Input, Output, callback
import plotly.graph_objs as go
import pandas as pd
from data.queries import asignaturas_superadas
from util import list_to_tuple


@callback(
    Output("graph-evolucion-progreso-academico", "figure"),
    Input("selected-alumnado-store", "data"),
    Input("curso-academico", "value"),
    Input("titulacion-alumnado", "value"),
)
def update_graph_alumnado(alumno_id, curso_academico, titulacion):
    """
    Actualiza el gráfico de evolución del progreso académico del perfil "Alumno"
    de la pestaña "Expediente académico personal".

    Args:
        alumno_id (str): Identificador del alumno.
        curso_academico (list): Lista con los cursos académicos
        titulacion (str): Titulación seleccionada

    Returns:
    go.Figure: Figura con el gráfico
    
    """

    fig = go.Figure()

    fig.update_layout(
        title={"text": "Evolución del progreso académico", "x": 0.5},
        xaxis={"title": "Curso académico"},
        yaxis={"title": "Nº Asignaturas de superadas"},
        showlegend=False,
    )

    if not (alumno_id and curso_academico and titulacion):
        return fig

    try:
        curso_academico = list_to_tuple(curso_academico)
    except Exception as e:
        print("Error:", e)
        return fig

    data = asignaturas_superadas(alumno_id, curso_academico, titulacion)

    if not data:
        return fig

    data = pd.DataFrame(data)
    academic_years = data["curso_academico"]
    subjects_passed = data["n_asig_superadas"]

    cumulative_passed = []
    cumulative_total = 0
    for count in subjects_passed:
        cumulative_total += count
        cumulative_passed.append(cumulative_total)

    fig.add_trace(
        go.Bar(x=academic_years, y=cumulative_passed, marker_color="blue", opacity=0.7)
    )

    return fig
