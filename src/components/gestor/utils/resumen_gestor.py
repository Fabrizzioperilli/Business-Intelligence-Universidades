#
# @file resumen_gestor.py
# @brief Este fichero contiene el componente para mostrar un resumen de los datos del gestor seleccionado.
# @version 1.0
# @date 21/05/2024
# @license MIT License
# @author Fabrizzio Daniell Perilli Martín
# @email alu0101138589@ull.edu.es
#

from dash import html
from callbacks.gestor.utils.callback_resumen_gestor import update_resumen_gestor


def resumen_gestor():
    """
    Crea un contenedor para mostrar un resumen de los datos del gestor seleccionado.
    
    Returns:
        html.Div: Contenedor para mostrar el resumen
    """
    
    return html.Div([], id="resumen-gestor")
