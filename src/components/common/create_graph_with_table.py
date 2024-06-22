#
# @file create_graph_with_table.py
# @brief Este archivo contiene la función para crear un gráfico con un modal para mostrar los datos y descargarlos.
# @version 1.0
# @date 14/06/2024
# @license MIT License
# @author Fabrizzio Daniell Perilli Martín
# @email alu0101138589@ull.edu.es
#

from components.common.create_graph import create_graph
from components.common.modal_data import create_modal
from dash import html


def create_graph_with_table(graph_id, item_class, config, modal_config):
    """
    Crea un gráfico con un modal para mostrar los datos y descargarlos.

    Args:
        graph_id (str): ID del gráfico
        item_class (str): Clase del gráfico
        config (dict): Configuración del gráfico
        modal_config (dict): Configuración del modal

    Returns:
        html.Div: Gráfico con modal para mostrar los datos
    """
    return html.Div(
        [create_graph(graph_id, item_class, config), create_modal(**modal_config)],
        className=item_class,
    )
