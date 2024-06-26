#
# @file filter_titulacion_alumnado.py
# @brief Este archivo contiene componente para filtrar titulaciones del alumnado.
# @version 1.0
# @date 18/05/2024
# @license MIT License
# @author Fabrizzio Daniell Perilli Martín
# @email alu0101138589@ull.edu.es
#

from dash import html, dcc
from callbacks.alumnado.filters.callback_filter_titulacion_alumnado import update_filter_titulacion_alumnado


def filter_titulacion_alumnado():
    """
    Crea un componente con un dropdown que contiene las titulaciones del perfil "Alumno".

    Returns:
        html.Div: Componente con un dropdown y almacenamiento de la titulación seleccionada
    """
    return html.Div(
        [
            html.Label("Titulación"),
            dcc.Dropdown(
                id="titulacion-alumnado",
                options=[],
                value=None,
                searchable=False,
                clearable=False,
                optionHeight=50,
                maxHeight=300,
                placeholder="Seleccione una opción",
            ),
            dcc.Store(id="selected-titulacion-alumnado-store", storage_type="local"),
        ]
    )
