#
# @file graphs_riesgo_abandono_gestor.py
# @brief Este fichero contiene el componente que muestra los gráficos 
#        de los indicadores de riesgo de abandono del perfil "Gestor"
# @version 1.0
# @date 26/05/2024
# @license MIT License
# @author Fabrizzio Daniell Perilli Martín
# @email alu0101138589@ull.edu.es
#

from dash import html
from callbacks.gestor.graphs.riesgo_abandono.callback_graph_tasa_abandono_gestor import update_graph_gestor
from callbacks.gestor.graphs.riesgo_abandono.callback_graph_tasa_graduacion_gestor import update_graph_gestor
from components.common.create_graph_with_table import create_graph_with_table
from util import config_mode_bar_buttons_gestor


def graphs_riesgo_abandono_gestor():
    """
    Retorna los gráficos de la pestaña "Riesgo de abandono" del perfil 
    "Gestor". Incluye un modal y una tabla para cada gráfico.

    Returns:
        html.Div: Gráficos
    """
    graphs_info = [
        {
            "graph_id": "tasa-abandono-gestor",
            "modal_id": "modal-tasa-abandono",
            "table_container_id": "table-container-tasa-abandono",
            "download_button_id": "btn-descargar-tasa-abandono",
            "view_data_button_id": "btn-ver-datos-tasa-abandono",
        },
        {
            "graph_id": "tasa-graduacion-gestor",
            "modal_id": "modal-tasa-graduacion",
            "table_container_id": "table-container-tasa-graduacion",
            "download_button_id": "btn-descargar-tasa-graduacion",
            "view_data_button_id": "btn-ver-datos-tasa-graduacion",
        },
    ]

    graph_elements = [
        create_graph_with_table(
            graph_info["graph_id"],
            "graph-item-riesgo-abandono-gestor",
            config_mode_bar_buttons_gestor,
            {
                "modal_id": graph_info["modal_id"],
                "table_container_id": graph_info["table_container_id"],
                "download_button_id": graph_info["download_button_id"],
                "view_data_button_id": graph_info["view_data_button_id"],
            },
        )
        for graph_info in graphs_info
    ]

    return html.Div(graph_elements, className="graphs-container-riesgo-abandono-gestor")
