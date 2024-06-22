#
# @file docente_layout.py
# @brief Este archivo contiene el código del layout del perfil "Docente".
# @version 1.0
# @date 01/05/2024
# @license MIT License
# @author Fabrizzio Daniell Perilli 
# @email alu0101138589@ull.edu.es
#

from dash import html
import components.docente.utils.tabs_docente as tabs_docente


def docente_layout():
    #
    # @brief Retorna el layout del perfil "Docente"
    # @return Layout del docente
    #
    return html.Div([tabs_docente.tabs_docente()])
