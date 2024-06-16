from dash import html


def filters(filters):
    """
    Crea un componente que contiene los filtros de la aplicación.
    
    Args:
    filters (list): Lista de filtros

    Returns:
    html.Div: Componente que contiene los filtros
    """
    return html.Div([html.H2("Filtros"), html.Div(filters)], className="filters")
