#
# @file filter_asignaturas_matri_alumnado.py
# @brief Este archivo contiene componente para filtrar asignaturas matriculadas por el alumno.
# @version 1.0
# @date 07/05/2024
# @license MIT License
# @author Fabrizzio Daniell Perilli Martín
# @email alu0101138589@ull.edu.es
#

from dash import html, dcc
from callbacks.alumnado.filters.callback_filter_asignaturas_matri_alumnado import update_filter_asignaturas_matri_alumnado


def filter_asignaturas_matri_alumnado():
    """
    Crea un componente con un dropdown que contiene las asignaturas matriculadas por el alumno.
    
    Returns:
        html.Div: Componente con un dropdown y un botón para seleccionar todas las asignaturas
    """
    return html.Div(
        [
            html.Br(),
            html.Label("Asignaturas matriculadas"),
            dcc.Dropdown(
                id="asignaturas-matriculadas",
                searchable=True,
                multi=True,
                value=None,
                clearable=True,
                options=[],
                maxHeight=300,
                optionHeight=50,
                placeholder="Seleccione una opción",
            ),
            html.Button(
                "Seleccionar todo",
                id="select-all-button",
                className="button-select-all-filter",
                n_clicks=0,
            ),
        ]
    )
