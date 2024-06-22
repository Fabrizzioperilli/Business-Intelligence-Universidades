#
# @file select_docente.py
# @brief Este fichero contiene el componente para seleccionar un docente.
# @version 1.0
# @date 14/05/2024
# @license MIT License
# @author Fabrizzio Daniell Perilli Martín
# @email alu0101138589@ull.edu.es
#

from dash import html, dcc
from callbacks.docente.utils.callback_select_docente import store_selected_docente


def select_docente():
    """
    Crea el desplegable para seleccionar un docente.
    
    Returns:
        html.Div: Desplegable para seleccionar un docente
    """
    return html.Div(
        [
            html.Div(
                [
                    dcc.Dropdown(
                        options=[],
                        value=None,
                        id="docente-dropdown",
                        clearable=False,
                        placeholder="Selecciona un docente",
                    )
                ],
                className="select-docente",
            ),
        ]
    )
