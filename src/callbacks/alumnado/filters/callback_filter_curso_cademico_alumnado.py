#
# @file callback_filter_curso_cademico_alumnado.py
# @brief Este fichero contiene el callback para actualizar el filtro de curso académico del alumnado
# @version 1.0
# @date 05/05/2024
# @license MIT License
# @author Fabrizzio Daniell Perilli Martín
# @email alu0101138589@ull.edu.es
#

from dash import Input, Output,State, callback, callback_context
from callbacks.alumnado.utils.callback_select_alumnado import store_selected_alumnado
from data.queries import curso_academico_alumnado

@callback(
    Output('curso-academico', 'options'),
    Output('curso-academico', 'value'),
    Input('selected-alumnado-store', 'data'),
    Input('titulacion-alumnado', 'value'),
    Input('select-all-cursos-academicos', 'n_clicks'),
    State('curso-academico', 'options')
)
def update_filter_curso_academico_alumnado(alumno_id, titulacion, n_clicks, existing_options):
    """
    Actualiza las opciones del dropdown de cursos académicos y
    gestiona el evento del botón "Seleccionar todo".

    Args:
        alumno_id (str): Identificador del alumno.
        titulacion (str): Titulación seleccionada
        n_clicks (int): Número de clicks en el botón "Seleccionar todo"
        existing_options (list): Opciones actuales del dropdown

    Returns:
        list: Opciones del dropdown
        list: Valor seleccionado
    """
    
    ctx = callback_context
    trigger_id = ctx.triggered[0]['prop_id'].split('.')[0] if ctx.triggered else None

    # Evento de selección de todos los cursos académicos
    if trigger_id == 'select-all-cursos-academicos' and n_clicks > 0:
        return existing_options, [option['value'] for option in existing_options]

    if not (alumno_id and titulacion):
        return [], None

    # Obtener los cursos académicos desde la base de datos
    data = curso_academico_alumnado(alumno_id, titulacion)

    if not data:
        return [], None

    opciones_dropdown = [{'label': curso[0], 'value': curso[0]} for curso in data]
    value = [option['value'] for option in opciones_dropdown]

    return opciones_dropdown, value
    