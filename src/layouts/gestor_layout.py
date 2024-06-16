from dash import html
import components.gestor.utils.tabs_gestor as tabs_gestor


def gestor_layout():
    return html.Div([tabs_gestor.tabs_gestor()])
