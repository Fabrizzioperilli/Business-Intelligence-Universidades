
from dash import html, callback, Output, Input, State
import components.alumnado.tabs_alumnado as tabs_alumnado
import components.alumnado.sidebar_alumnado as sidebar_alumnado
import dash_bootstrap_components as dbc

def alumno_layout():
    return html.Div([
        tabs_alumnado.tabs_alumnado(),
        
        
    ])
    
    
@callback(Output('tabs-alumnado-content', 'children'),
            [Input('tabs-alumnado', 'value')])
def render_content(tab):
    if tab == 'expediente-personal-tab':
        return html.Div([
            toggle_button,
            sidebar_collapse
        ])
    elif tab == 'rendimiento-academico-tab':
        return html.Div([
            html.H3("Rendimiento Académico")
        ])
    else:
        return html.Div([
            html.H3("Expediente Académico Personal")
        ])
        
        
toggle_button =  dbc.Button(
        html.Img(src='assets/images/icon_sidebar.png', height="40px", width="40px"), 
        id="sidebar-toggle"
    )

sidebar_collapse = dbc.Collapse(
    sidebar_alumnado.sidebar_alumnado(),
    id="collapse",
    is_open=True
)

@callback(
    Output("collapse", "is_open"),
    [Input("sidebar-toggle", "n_clicks")],
    [State("collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open