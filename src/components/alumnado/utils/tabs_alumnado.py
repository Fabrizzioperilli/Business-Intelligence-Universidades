#
# @file tabs_alumnado.py
# @brief Este archivo contiene el componente para las pestañas del perfil "Alumnado".
# @version 1.0
# @date 28/04/2024
# @license MIT License
# @author Fabrizzio Daniell Perilli Martín
# @email alu0101138589@ull.edu.es
#

from dash import html, dcc
from callbacks.alumnado.utils.callback_tabs_alumnado import render_content


def tabs_alumnado():
    """
    Contiene las pestañas de la vista del alumnado.

    Returns:
        html.Div: Pestañas del alumnado
    """
    return html.Div(
        [
            dcc.Tabs(
                id="tabs-alumnado",
                value="expediente-personal-tab",
                children=[
                    dcc.Tab(
                        label="Expediente académico personal",
                        value="expediente-personal-tab",
                    ),
                    dcc.Tab(
                        label="Rendimiento académico general",
                        value="rendimiento-academico-tab",
                    ),
                    dcc.Tab(label="Recomendaciones", value="recomendador-tab"),
                ],
                className="tabs",
            ),
            html.Div(id="tabs-alumnado-content"),
            dcc.Store(id="selected-alumnado-store", storage_type="local"),
            dcc.Location(id="url", refresh=False),
        ]
    )
