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
