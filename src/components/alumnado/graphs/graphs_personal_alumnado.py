#
# @file graphs_personal_alumnado.py
# @brief Este archivo contiene el componente para los gráficos del perfil "Alumnado".
# @version 1.0
# @date 07/05/2024
# @license MIT License
# @author Fabrizzio Daniell Perilli Martín
# @email alu0101138589@ull.edu.es
#

from dash import html
from callbacks.alumnado.graphs.personal.callback_graph_calif_cualitativa_alumnado import update_graph_alumnado
from callbacks.alumnado.graphs.personal.callback_graph_progreso_academico_alumnado import update_graph_alumnado
from callbacks.alumnado.graphs.personal.callback_graph_calif_numerica_alumnado import update_graph_alumnado
from callbacks.alumnado.graphs.personal.callback_graph_tasa_rendimiento_alumnado import update_graph_alumnado
from components.common.create_graph import create_graph


def graphs_personal_alumnado():
    """
    Retorna los gráficos de la pestaña "Expediente académico Personal" del perfil "Alumnado"

    Returns:
        html.Div: Gráficos
    """
    graph_ids = [
        "graph-evolucion-progreso-academico",
        "graph-bar-evolucion-asignaturas-matriculadas",
        "graph-bar-calificaciones-por-asignatura",
        "graph-bar-tasa-rendimiento",
    ]

    config = {"displayModeBar": False}
    item_class = "graph-item-personal-alumnado"

    return html.Div(
        [create_graph(graph_id, item_class, config) for graph_id in graph_ids],
        className="graphs-container-personal-alumnado",
    )
