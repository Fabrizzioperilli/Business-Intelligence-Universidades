#
# @file callback_filter_curso_academico_gestor.py
# @brief Este fichero contiene el callback para actualizar las opciones 
#        del filtro de curso académico del perfil "Gestor" en la 
#        pestaña "Indicadores académicos".
# @version 1.0
# @date 21/05/2024
# @license MIT License
# @author Fabrizzio Daniell Perilli Martín
# @email alu0101138589@ull.edu.es
#

from dash import Input, Output, callback
from data.queries import universidades_gestor, curso_academico_universidad


@callback(
    Output("curso-academico-gestor", "options"),
    Output("curso-academico-gestor", "value"),
    Input("selected-gestor-store", "data"),
)
def update_filter_curso_academico_gestor(gestor_id):
    """
    Actualiza las opciones del filtro de curso académico del perfil "Gestor" 
    en la pestaña "Indicadores académicos".

    Args:
        gestor_id (str): ID del gestor seleccionado
    
    Returns:
        list: Opciones del dropdown
        str: Valor seleccionado
    """

    if not gestor_id:
        return [], None

    cod_universidad = universidades_gestor(gestor_id)

    if not cod_universidad:
        return [], None

    data = curso_academico_universidad(cod_universidad[0][0])

    if not data:
        return [], None

    opciones_dropdown = [{"label": curso[0], "value": curso[0]} for curso in data]
    value = opciones_dropdown[0]["value"] if opciones_dropdown else None

    return opciones_dropdown, value
