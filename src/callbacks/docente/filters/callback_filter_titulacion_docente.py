#
# @file callback_filter_titulacion_docente.py
# @brief Este fichero contiene el callback para actualizar las opciones
#        del dropdown con las titulaciones del docente seleccionado.
# @version 1.0
# @date 19/05/2024
# @license MIT License
# @author Fabrizzio Daniell Perilli Martín
# @email alu0101138589@ull.edu.es
#

from dash import Input, Output, State, callback
from data.queries import titulacion_docente

@callback(
  Output('titulacion-docente', 'options'),
  Output('titulacion-docente', 'value'),
  Output('selected-titulacion-docente-store', 'data'),
  Input('selected-docente-store', 'data'),
  Input('titulacion-docente', 'value'),
  State('selected-titulacion-docente-store', 'data')
)
def update_filter_titulacion_docente(docente_id, selected_value, stored_titulacion):
    """
    Actualiza las opciones del dropdown con las titulaciones del docente seleccionado.
    
    Args:
        docente_id (str): ID del docente
        selected_value (str): Valor seleccionado
        stored_titulacion (str): Titulación seleccionada
    
    Returns:
        list: Opciones del dropdown
        str: Valor seleccionado
    
    """
    if not docente_id:
        return [], None, None
    
    data = titulacion_docente(docente_id)
    
    if not data:
        return [], None, None
    
    opciones_dropdown = [{'label': asignatura[0], 'value': asignatura[0]} for asignatura in data]

    if selected_value is None and stored_titulacion in [op['value'] for op in opciones_dropdown]:
        return opciones_dropdown, stored_titulacion, stored_titulacion
        
    return opciones_dropdown, selected_value, selected_value

    