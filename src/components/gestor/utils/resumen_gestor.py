from dash import html
from callbacks.gestor.utils.callback_resumen_gestor import update_resumen_gestor


def resumen_gestor():
    """
    Crea un contenedor para mostrar un resumen de los datos del gestor seleccionado.
    
    Returns:
    html.Div: Contenedor para mostrar el resumen
    """
    
    return html.Div([], id="resumen-gestor")
