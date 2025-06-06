#
# @file filter_curso_academico_docente.py
# @brief Este fichero contiene el componente de in filtro que contiene los cursos académicos del perfil "Docente"
# @version 1.0
# @date 20/05/2024
# @license MIT License
# @author Fabrizzio Daniell Perilli Martín
# @email alu0101138589@ull.edu.es
#
from dash import html, dcc
from callbacks.docente.filters.callback_filter_curso_academico_docente import update_filter_curso_academico_docente


def filter_curso_academico_docente():
    """
    Crea un componente con un dropdown que contiene los cursos académicos del perfil "Docente"
    en la pestaña "Rendimiento académico personal".

    Returns:
        html.Div: Componente con un dropdown
    """
    return html.Div(
        [
            html.Br(),
            html.Label("Curso académico"),
            dcc.Dropdown(
                id="curso-academico-docente",
                searchable=False,
                multi=True,
                clearable=True,
                options=[],
                value=None,
                maxHeight=300,
            ),
            html.Button(
                "Seleccionar todo",
                id="select-all-cursos-academicos-docente",
                className="button-select-all-filter",
                n_clicks=0,
            ),
        ]
    )
