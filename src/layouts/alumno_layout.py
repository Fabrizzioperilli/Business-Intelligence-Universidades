from dash import html
import components.alumnado.utils.tabs_alumnado as tabs_alumnado


def alumno_layout():
    """
    Retorna el layout del perfil "Alumno"

    Returns:
    html.Div: Layout del alumno
    """
    return html.Div([tabs_alumnado.tabs_alumnado()])
