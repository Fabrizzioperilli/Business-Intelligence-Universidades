from dash import html
import components.alumnado.resumen_alumnado as resumen_alumnado
import components.common.filters as filters
import dash_bootstrap_components as dbc
from callbacks.common.callback_sidebar_collapse import sidebar_collapse

def sidebar(components):
    toggle_button = dbc.Button(
        html.Img(src='assets/images/icon_sidebar.png', height="40px", width="40px"), 
        id="sidebar-toggle"
    )

    sidebar_content = html.Div(components, className='sidebar')

    sidebar_collapse = dbc.Collapse(
        sidebar_content,
        id="collapse",
        is_open=True
    )

    return html.Div([toggle_button, sidebar_collapse])