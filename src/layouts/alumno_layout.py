#
# @file alumno_layout.py
# @brief Este archivo contiene el código del layout del perfil "Alumno".
# @version 1.0
# @date 01/05/2024
# @license MIT License
# @author Fabrizzio Daniell Perilli 
# @email alu0101138589@ull.edu.es
#

from dash import html
import components.alumnado.utils.tabs_alumnado as tabs_alumnado


def alumno_layout():
    #
    # @brief Retorna el layout del perfil "Alumno"
    # @return Layout del alumno
    #
    return html.Div([tabs_alumnado.tabs_alumnado()])
