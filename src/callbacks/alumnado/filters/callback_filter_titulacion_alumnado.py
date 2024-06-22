#
# @file callback_filter_titulacion_alumnado.py
# @brief Este fichero contiene el callback para actualizar las titulaciones del alumnado
# @version 1.0
# @date 18/05/2024
# @license MIT License
# @author Fabrizzio Daniell Perilli Martín
# @email alu0101138589@ull.edu.es
#

from dash import Input, Output, State, callback
from data.queries import titulacion_alumnado

@callback(
    Output('titulacion-alumnado', 'options'),
    Output('titulacion-alumnado', 'value'),
    Output('selected-titulacion-alumnado-store', 'data'),
    Input('selected-alumnado-store', 'data'),
    Input('titulacion-alumnado', 'value'),
    State('selected-titulacion-alumnado-store', 'data')
)
def update_filter_titulacion_alumnado(alumno_id, selected_value, stored_titulacion):
    """
    Actualiza las opciones del dropdown de titulaciones del perfil "Alumno".

    Args:
        alumno_id (str): Identificador del alumno.
        selected_value (str): Valor seleccionado en el dropdown
        stored_titulacion (str): Titulación almacenada

    Returns:
        list: Opciones del dropdown
        str: Valor seleccionado
    """
    if not alumno_id:
        return [], None, None
    
    data = titulacion_alumnado(alumno_id)
    
    if not data:
        return [], None, None
    
    opciones_dropdown = [{'label': asignatura[0], 'value': asignatura[0]} for asignatura in data]
    
    # Si no hay valor seleccionado pero hay un valor almacenado, lo usamos si está en las opciones
    if selected_value is None and stored_titulacion in [op['value'] for op in opciones_dropdown]:
        return opciones_dropdown, stored_titulacion, stored_titulacion
    
    return opciones_dropdown, selected_value, selected_value
