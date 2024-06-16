from components.common.create_graph import create_graph
from components.common.modal_data import create_modal
from dash import html


def create_graph_with_table(graph_id, item_class, config, modal_config):
    """
    Crea un gráfico con un modal para mostrar los datos y descargarlos.

    :param graph_id: str: ID del gráfico.
    :param item_class: str: Clase del item.
    :param config: dict: Configuración del gráfico.
    :param modal_config: dict: Configuración del modal.
    :return: html.Div: Gráfico con modal.
    """
    return html.Div(
        [create_graph(graph_id, item_class, config), create_modal(**modal_config)],
        className=item_class,
    )
