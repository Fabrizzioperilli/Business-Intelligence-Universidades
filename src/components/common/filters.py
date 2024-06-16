from dash import html


def filters(filters):
    """
    Crea un componente que contiene los filtros de la aplicación.
    
    :param filters: list: Lista de filtros.
    :return: html.Div: Componente que contiene los filtros.
    """
    return html.Div([html.H2("Filtros"), html.Div(filters)], className="filters")
