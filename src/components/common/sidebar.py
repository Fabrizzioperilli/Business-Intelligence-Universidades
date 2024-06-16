from dash import html
import dash_bootstrap_components as dbc
from callbacks.common.callback_sidebar_collapse import sidebar_collapse


def sidebar(components):
    """
    Sidebar del dashboard donde se encuentra el resumen de la información y los filtros

    Args:
    components (list): Componentes que se desplegarán en el sidebar

    Returns:
    html.Div: Sidebar del dashboard
    
    """
    sidebar_content = html.Div(components, className="sidebar")
    sidebar_collapse = dbc.Collapse(sidebar_content, id="collapse", is_open=True)

    return html.Div(sidebar_collapse)
