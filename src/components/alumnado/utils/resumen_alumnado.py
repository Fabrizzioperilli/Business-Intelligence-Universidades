#
# @file resumen_alumnado.py
# @brief Este archivo contiene el componente para el resumen del perfil "Alumnado".
# @version 1.0
# @date 28/04/2024
# @license MIT License
# @author Fabrizzio Daniell Perilli Martín
# @email alu0101138589@ull.edu.es
#

from dash import html
from callbacks.alumnado.utils.callback_resumen_alumnado import update_resumen_alumnado


def resumen_alumnado():
    """
    Crea el layout del resumen del alumnado.

    Returns:
        html.Div: Layout del resumen del alumnado
    """
    return html.Div([], id="resumen-alumnado")
