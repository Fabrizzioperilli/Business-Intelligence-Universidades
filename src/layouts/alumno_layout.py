from dash import html
import components.alumnado.tabs_alumnado as tabs_alumnado

def alumno_layout():
    return html.Div([
        tabs_alumnado.tabs_alumnado()
    ])
    
