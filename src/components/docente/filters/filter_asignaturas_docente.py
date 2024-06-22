#
# @file filter_asignaturas_docente.py
# @brief Este fichero contiene el componente de un filtro con un dropdown que contiene las asignaturas del perfil "Docente"
# @version 1.0
# @date 15/05/2024
# @license MIT License
# @author Fabrizzio Daniell Perilli Martín
# @email alu0101138589@ull.edu.es
#

from dash import html, dcc
from callbacks.docente.filters.callback_filter_asignaturas_docente import update_filter_asignaturas_docente


def filter_asignaturas_docente():
    """
    Crea un componente con un dropdown que contiene las asignaturas del perfil "Docente"
    en la pestaña "Rendimiento académico personal".

    Returns:
        html.Div: Componente con un dropdown
    """

    return html.Div([
        html.Br(),
        html.Label("Asignaturas"),
        dcc.Dropdown(
            id="asignaturas-docente",
            searchable=True,
            value=None,
            clearable=True,
            options=[],
            maxHeight=300,
            optionHeight=50,
        )
    ])
