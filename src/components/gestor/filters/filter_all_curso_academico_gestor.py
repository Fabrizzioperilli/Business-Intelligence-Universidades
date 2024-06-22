#
# @file filter_all_curso_academico_gestor.py
# @brief Este fichero contiene el componente de filtro que contiene 
#        todos los cursos académicos para el perfil "Gestor"
# @version 1.0
# @date 27/05/2024
# @license MIT License
# @author Fabrizzio Daniell Perilli Martín
# @email alu0101138589@ull.edu.es
#

from dash import html, dcc
from callbacks.gestor.filters.callback_filter_all_curso_academico_gestor import update_filter_all_curso_academico_gestor


def filter_all_curso_academico_gestor():
    """
    Crea el filtro que muestra todos los cursos académicos disponibles
    para el perfil "Gestor" de la pestaña "Riesgo académico".

    Returns:
        html.Div: Componente con el filtro de curso académico
    """

    return html.Div(
        [
            html.Label("Curso académico"),
            dcc.Dropdown(
                id="curso-all-academico-gestor",
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
                id="select-all-curso-academico-button",
                className="button-select-all-filter",
                n_clicks=0,
            ),
            dcc.Store(id="curso-all-academico-gestor-store", storage_type="local"),
        ]
    )
