#
# @file graphs_general_docente.py
# @brief Este fichero contiene el componente que muestra los gráficos del perfil 
#       "Docente" en la pestaña "Rendimiento académico general"
# @version 1.0
# @date 16/05/2024
# @license MIT License
# @author Fabrizzio Daniell Perilli Martín
# @email alu0101138589@ull.edu.es
#

from dash import html
from callbacks.docente.graphs.general.callback_graph_all_calif_cualitativa_docente import update_graph_docente
from callbacks.docente.graphs.general.callback_graph_all_calif_media_docente import update_graph_docente
from components.common.create_graph import create_graph
from util import config_mode_bar_buttons_gestor


def graphs_general_docente():
    """
    Retorna los gráficos de la pestaña "Rendimiento académico general" 
    del perfil "Docente"

    Returns:
        html.Div: Gráficos
    """

    graphs_ids = [
        "calificaiones-cuali-all-asig-docente",
        "calificaiones-media-all-asig-docente",
    ]

    item_class = "graph-item-general-docente"
    config = config_mode_bar_buttons_gestor

    return html.Div(
        [create_graph(graph_id, item_class, config) for graph_id in graphs_ids],
        className="graphs-container-general-docente",
    )
