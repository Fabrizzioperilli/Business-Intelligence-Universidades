#
# @file callback_filter_all_asignaturas_titulacion_docente.py
# @brief Este fichero contiene el callback para actualizar las opciones 
#        del dropdown con todas las asignaturas de la titulación seleccionada 
#        y gestionar el evento del botón que selecciona todas las asignaturas.
# @version 1.0
# @date 20/05/2024
# @license MIT License
# @author Fabrizzio Daniell Perilli Martín
# @email alu0101138589@ull.edu.es
#

from dash import Input, Output, State, callback, callback_context
from data.queries import asignaturas_actas_titulacion


@callback(
    Output("all-asignaturas-titulacion-docente", "options"),
    Output("all-asignaturas-titulacion-docente", "value"),
    Input("titulacion-docente", "value"),
    Input("all-cursos-academicos-docente", "value"),
    Input("select-all-asignaturas-titulacion-docente", "n_clicks"),
    State("all-asignaturas-titulacion-docente", "options"),
)
def update_filter_asignaturas_docente(titulacion, curso_academico, n_clicks, existing_options):
    """
    Actualiza las opciones del dropdown con todas las asignaturas de la titulación seleccionada y
    gestiona el evento del botón que selecciona todas las asignaturas.
    
    Args:
        titulacion (str): Titulación seleccionada
        curso_academico (list): Cursos académicos seleccionados
        n_clicks (int): Número de clicks en el botón "Seleccionar todo"
        existing_options (list): Opciones actuales del dropdown
    
    Returns:
        list: Opciones del dropdown
        list: Valor seleccionado
    """
    ctx = callback_context
    trigger_id = ctx.triggered[0]["prop_id"].split(".")[0] if ctx.triggered else None

    if trigger_id == "select-all-asignaturas-titulacion-docente" and n_clicks > 0:
        return existing_options, [option["value"] for option in existing_options]

    if not (titulacion and curso_academico):
        return [], None

    data = asignaturas_actas_titulacion(titulacion, curso_academico)

    if not data:
        return [], None

    opciones_dropdown = [
        {"label": asignatura[0], "value": asignatura[0]} for asignatura in data
    ]
    value = (
        [option["value"] for option in opciones_dropdown] if opciones_dropdown else []
    )

    return opciones_dropdown, value
