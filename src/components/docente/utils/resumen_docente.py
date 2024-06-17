from dash import html
from callbacks.docente.utils.callback_resumen_docente import update_resumen_docente


def resumen_docente():
    """
    Crea el layout del resumen del docente

    Returns:
    html.Div: Layout del resumen del docente
    """
    return html.Div([], id="resumen-docente")
