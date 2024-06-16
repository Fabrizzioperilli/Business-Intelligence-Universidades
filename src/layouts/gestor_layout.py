from dash import html
import components.gestor.utils.tabs_gestor as tabs_gestor


def gestor_layout():
    """
    Retorna el layout del perfil "Gestor"

    Returns:
    html.Div: Layout del gestor
    """
    return html.Div([tabs_gestor.tabs_gestor()])
