from dash import html
import components.alumnado.resumen_alumnado as resumen_alumnado
import components.alumnado.filters_alumnado as filters_alumnado
import dash_bootstrap_components as dbc
from callbacks.alumnado.callback_toggle_collapse_alumnado import toggle_collapse

def sidebar_alumnado():
    return html.Div([
      resumen_alumnado.resumen_alumnado(),
      filters_alumnado.filters_alumnado(),
    ], className='sidebar')
  

toggle_button =  dbc.Button(
        html.Img(src='assets/images/icon_sidebar.png', height="40px", width="40px"), 
        id="sidebar-toggle"
    )

sidebar_collapse_alumnado = dbc.Collapse(
    sidebar_alumnado(),
    id="collapse",
    is_open=True
)
  