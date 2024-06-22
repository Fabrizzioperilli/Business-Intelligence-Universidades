#
# @file graphs_resultados_gestor.py
# @brief Este fichero contiene el componente que muestra los gráficos 
#        de los resultados académicos del perfil "Gestor"
# @version 1.0
# @date 22/05/2024
# @license MIT License
# @author Fabrizzio Daniell Perilli Martín
# @email alu0101138589@ull.edu.es
#

from dash import html
from callbacks.gestor.graphs.resultados.callback_graph_nota_acceso_titulacion_gestor import update_grpht_gestor
from callbacks.gestor.graphs.resultados.callback_graph_duracion_media_estudios_nota_gestor import update_graph_gestor
from components.common.create_graph_with_table import create_graph_with_table
from util import config_mode_bar_buttons_gestor


def graphs_resultados_gestor():
    """
    Retorna los gráficos de la pestaña "Resultados académicos" del perfil 
    "Gestor". Incluye un modal y una tabla para cada gráfico.

    Returns:
        html.Div: Gráficos
    """
    graphs_info = [
        {
            "graph_id": "duración-estudios-nota-media-gestor",
            "modal_id": "modal-duracion-estudios",
            "table_container_id": "table-container-duracion-estudios",
            "download_button_id": "btn-descargar-csv-duracion-estudios",
            "view_data_button_id": "btn-ver-datos-duracion-estudios",
        },
        {
            "graph_id": "nota-acceso-titulacion",
            "modal_id": "modal-nota-acceso",
            "table_container_id": "table-container-nota-acceso",
            "download_button_id": "btn-descargar-csv-nota-acceso",
            "view_data_button_id": "btn-ver-datos-nota-acceso",
        },
    ]

    graph_elements = [
        create_graph_with_table(
            graph_info["graph_id"],
            "graph-item-resultados-gestor",
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

    return html.Div(graph_elements, className="graphs-container-resultados-gestor")
