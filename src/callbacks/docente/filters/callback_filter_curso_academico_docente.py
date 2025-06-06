#
# @file callback_filter_curso_academico_docente.py
# @brief Este fichero contiene el callback para actualizar las opciones
#        del dropdown con los cursos académicos del docente seleccionado y
#        gestionar el evento del botón que selecciona todos los cursos académicos.
# @version 1.0
# @date 15/05/2024
# @license MIT License
# @author Fabrizzio Daniell Perilli Martín
# @email alu0101138589@ull.edu.es
#

from dash import Input, Output, callback, State, callback_context
from data.queries import curso_academico_docente
from callbacks.docente.utils.callback_select_docente import store_selected_docente


@callback(
    Output("curso-academico-docente", "options"),
    Output("curso-academico-docente", "value"),
    Input("selected-docente-store", "data"),
    Input("asignaturas-docente", "value"),
    Input("select-all-cursos-academicos-docente", "n_clicks"),
    State("curso-academico-docente", "options"),
)
def update_filter_curso_academico_docente(docente_id, asignatura, n_clicks, existing_options):
    """
    Actualiza las opciones del dropdown con los cursos académicos del docente seleccionado y
    gestiona el evento del botón que selecciona todos los cursos académicos.
    
    Args:
        docente_id (str): ID del docente
        asignatura (str): Asignatura seleccionada
        n_clicks (int): Número de clicks en el botón "Seleccionar todo"
        existing_options (list): Opciones actuales del dropdown
    
    Returns:
        list: Opciones del dropdown
        list: Valor seleccionado
        
    """
    ctx = callback_context
    trigger_id = ctx.triggered[0]["prop_id"].split(".")[0] if ctx.triggered else None

    if trigger_id == "select-all-cursos-academicos" and n_clicks > 0:
        return existing_options, [option["value"] for option in existing_options]

    if not (docente_id and asignatura):
        return [], None

    data = curso_academico_docente(docente_id, asignatura)

    if not data:
        return [], None

    opciones_dropdown = [{"label": curso[0], "value": curso[0]} for curso in data]
    value = [option["value"] for option in opciones_dropdown]

    return opciones_dropdown, value
