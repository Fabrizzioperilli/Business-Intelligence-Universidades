from dash import html
from callbacks.alumnado.utils.callback_resumen_alumnado import update_resumen_alumnado


def resumen_alumnado():
    """
    Crea el layout del resumen del alumnado.
    """
    return html.Div([], id="resumen-alumnado")
