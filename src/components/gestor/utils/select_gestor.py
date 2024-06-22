#
# @file select_gestor.py
# @brief Este fichero contiene el componente para seleccionar un gestor.
# @version 1.0
# @date 21/05/2024
# @license MIT License
# @author Fabrizzio Daniell Perilli Martín
# @email alu0101138589@ull.edu.es
#

from dash import html, dcc
from callbacks.gestor.utils.callback_select_gestor import store_selected_gestor


def select_gestor():
    """
    Crea un dropdown para seleccionar un gestor.
    
    Returns:
        html.Div: Dropdown para seleccionar un gestor
    """
    
    return html.Div(
        [
            html.Div(
                [
                    dcc.Dropdown(
                        options=[],
                        value=None,
                        id="gestor-dropdown",
                        clearable=False,
                        placeholder="Seleccione un gestor",
                    )
                ],
                className="select-gestor",
            ),
        ]
    )
