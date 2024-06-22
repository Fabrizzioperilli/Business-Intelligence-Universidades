#
# @file recomendador_docente.py
# @brief Este fichero contiene el componente del recomendador para docentes.
# @version 1.0
# @date 14/05/2024
# @license MIT License
# @author Fabrizzio Daniell Perilli Martín
# @email alu0101138589@ull.edu.es
#

from dash import html
from callbacks.docente.utils.callback_resumen_docente import update_resumen_docente


def resumen_docente():
    """
    Crea el layout del resumen del docente

    Returns:
        html.Div: Layout del resumen del docente
    """
    return html.Div([], id="resumen-docente")
