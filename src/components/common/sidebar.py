from dash import html
import dash_bootstrap_components as dbc
from callbacks.common.callback_sidebar_collapse import sidebar_collapse


def sidebar(components):
    sidebar_content = html.Div(components, className="sidebar")
    sidebar_collapse = dbc.Collapse(sidebar_content, id="collapse", is_open=True)

    return html.Div(sidebar_collapse)
