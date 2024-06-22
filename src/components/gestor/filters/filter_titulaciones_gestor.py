#
# @file filter_titulaciones_gestor.py
# @brief Este fichero contiene el componente de filtro que contiene 
#        las titulaciones para el perfil "Gestor"
# @version 1.0
# @date 21/05/2024
# @license MIT License
# @author Fabrizzio Daniell Perilli Martín
# @email alu0101138589@ull.edu.es
#

from dash import html, dcc
from callbacks.gestor.filters.callback_filter_titulaciones_gestor import update_filter_titulaciones_gestor


def filter_titulaciones_gestor():
    """
    Crea el filtro de titulaciones para el perfil "Gestor" de la pestaña
    "Indicadores académicos".

    Returns:
        html.Div: Componente con el filtro de titulaciones
    """
    return html.Div(
        [
            html.Br(),
            html.Label("Titulaciones"),
            dcc.Dropdown(
                id="titulaciones-gestor",
                searchable=True,
                multi=True,
                clearable=True,
                options=[],
                value=None,
                maxHeight=200,
                placeholder="Seleccione una opción",
            ),
            html.Button(
                "Seleccionar todo",
                id="select-all-titulaciones-gestor",
                className="button-select-all-filter",
                n_clicks=0,
            ),
        ]
    )
