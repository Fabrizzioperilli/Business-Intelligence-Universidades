#
# @file select_alumnado.py
# @brief Este archivo contiene el componente para seleccionar un alumno.
# @version 1.0
# @date 05/05/2024
# @license MIT License
# @author Fabrizzio Daniell Perilli Martín
# @email alu0101138589@ull.edu.es
#

from dash import html, dcc
from callbacks.alumnado.utils.callback_select_alumnado import store_selected_alumnado


def select_alumnado():
    """
    Crea el desplegable para seleccionar un alumno.

    Returns:
        html.Div: Desplegable para seleccionar un alumno
    """
    return html.Div(
        [
            html.Div(
                [
                    dcc.Dropdown(
                        options=[],
                        value=None,
                        id="alumnado-dropdown",
                        clearable=False,
                        placeholder="Seleccione un alumno",
                    )
                ],
                className="select-alumnado",
            ),
        ]
    )
