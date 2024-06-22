#
# @file gestor_layout.py
# @brief Este archivo contiene el código del layout del perfil "Gestor".
# @version 1.0
# @date 01/05/2024
# @license MIT License
# @author Fabrizzio Daniell Perilli Martín
# @email alu0101138589@ull.edu.es
#

from dash import html
import components.gestor.utils.tabs_gestor as tabs_gestor


def gestor_layout():
    #
    # @brief Retorna el layout del perfil "Gestor"
    # @return Layout del gestor
    #
    return html.Div([tabs_gestor.tabs_gestor()])
