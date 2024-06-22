#
# @file create_graph.py
# @brief Este archivo contiene la función para crear un gráfico con un id, una clase y una configuración específica.
# @version 1.0
# @date 14/06/2024
# @license MIT License
# @author Fabrizzio Daniell Perilli Martín
# @email alu0101138589@ull.edu.es
#

from dash import html, dcc


def create_graph(graph_id, item_class, config):
    """
    Crea un gráfico con un id, una clase y una configuración específica.

    Args:
        graph_id (str): ID del gráfico
        item_class (str): Clase del gráfico
        config (dict): Configuración del gráfico

    Returns:
        html.Div: Gráfico
    """
    return html.Div(
        [dcc.Loading(children=[dcc.Graph(id=graph_id, figure={}, config=config)])],
        className=item_class,
    )
