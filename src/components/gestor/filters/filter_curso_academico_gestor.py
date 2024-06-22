#
# @file filter_curso_academico_gestor.py
# @brief Este fichero contiene el componente de filtro que contiene 
#        el curso académico para el perfil "Gestor"
# @version 1.0
# @date 21/05/2024
# @license MIT License
# @author Fabrizzio Daniell Perilli Martín
# @email alu0101138589@ull.edu.es
#

from dash import html, dcc
from callbacks.gestor.filters.callback_filter_curso_academico_gestor import update_filter_curso_academico_gestor


def filter_curso_academico_gestor():
    """
    Crea el filtro de curso académico para el perfil "Gestor" de la pestaña
    "Indicadores académicos".

    Returns:
        html.Div: Componente con el filtro de curso académico
    """
    return html.Div(
        [
            html.Label("Curso académico"),
            dcc.Dropdown(
                id="curso-academico-gestor",
                searchable=True,
                multi=False,
                clearable=False,
                options=[],
                value=None,
                maxHeight=300,
                placeholder="Selecciona una opción",
            ),
        ]
    )
