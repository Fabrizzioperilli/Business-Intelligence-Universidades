from dash import html, callback, Output, Input
import components.gestor.tabs_gestor as tabs_gestor

def gestor_layout():
    return html.Div([
        tabs_gestor.tabs_gestor(),
    ])

    
