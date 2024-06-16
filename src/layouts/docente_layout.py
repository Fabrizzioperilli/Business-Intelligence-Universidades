from dash import html
import components.docente.utils.tabs_docente as tabs_docente


def docente_layout():
    """
    Retorna el layout del perfil "Docente"

    Returns:
    html.Div: Layout del docente
    """
    return html.Div([tabs_docente.tabs_docente()])
