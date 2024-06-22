#
# @file tabs_docente.py
# @brief Este fichero contiene el componente de las pestañas del perfil "Docente"
# @version 1.0
# @date 28/04/2024
# @license MIT License
# @author Fabrizzio Daniell Perilli Martín
# @email alu0101138589@ull.edu.es
#

from dash import html, dcc
from callbacks.docente.utils.callback_tabs_docente import render_content


def tabs_docente():
    """
    Crea las pestañas del perfil "Docente"
    
    Returns:
        html.Div: Pestañas del docente
    """
    
    return html.Div(
        [
            dcc.Tabs(
                id="tabs-docente",
                value="rendimiento-academico-asignatura-tab",
                children=[
                    dcc.Tab(
                        label="Rendimiento académico personal",
                        value="rendimiento-academico-asignatura-tab",
                    ),
                    dcc.Tab(
                        label="Rendimiento académico general",
                        value="rendimiento-academico-tab",
                    ),
                    dcc.Tab(label="Recomendaciones", value="recomendaciones-tab"),
                ],
                className="tabs",
            ),
            html.Div(id="tabs-docente-content"),
            dcc.Store(id="selected-docente-store", storage_type="local"),
        ]
    )
