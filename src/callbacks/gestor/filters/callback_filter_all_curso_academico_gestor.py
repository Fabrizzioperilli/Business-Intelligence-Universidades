#
# @file callback_filter_all_curso_academico_gestor.py
# @brief Este fichero contiene el callback para actualizar las opciones
#        del filtro de todos los cursos académicos del perfil "Gestor" en la pestaña "Riesgo académico".
# @version 1.0
# @date 27/05/2024
# @license MIT License
# @author Fabrizzio Daniell Perilli Martín
# @email alu0101138589@ull.edu.es
#

from dash import Input, Output, State, callback, callback_context
from data.queries import universidades_gestor, curso_academico_universidad


@callback(
    Output("curso-all-academico-gestor", "options"),
    Output("curso-all-academico-gestor", "value"),
    Input("selected-gestor-store", "data"),
    Input("select-all-curso-academico-button", "n_clicks"),
    State("curso-all-academico-gestor", "options"),
)
def update_filter_all_curso_academico_gestor(gestor_id, n_clicks, existing_options):
    """
    Actualiza las opciones del filtro de todos los cursos académicos del perfil "Gestor"
    en la pestaña "Riesgo académico".

    Args:
        gestor_id (str): ID del gestor seleccionado
        n_clicks (int): Número de clicks en el botón "Seleccionar todo"
        existing_options (list): Opciones actuales del filtro de curso académico

    Returns:
        list: Opciones del dropdown
        list: Valores seleccionados
    """

    ctx = callback_context
    trigger_id = ctx.triggered[0]["prop_id"].split(".")[0] if ctx.triggered else None

    if trigger_id == "select-all-curso-academico-button" and n_clicks > 0:
        return existing_options, [option["value"] for option in existing_options]

    if not gestor_id:
        return [], None

    cod_universidad = universidades_gestor(gestor_id)

    if not cod_universidad:
        return [], None

    data = curso_academico_universidad(cod_universidad[0][0])

    if not data:
        return [], None

    opciones_dropdown = [{"label": curso[0], "value": curso[0]} for curso in data]
    value = (
        [option["value"] for option in opciones_dropdown] if opciones_dropdown else []
    )

    return opciones_dropdown, value
