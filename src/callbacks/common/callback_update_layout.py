#
# @file callback_update_layout.py
# @brief Este fichero contiene el callback para actualizar el layout de 
#        la aplicación según el rol del usuario.
# @version 1.0
# @date 29/04/2024
# @license MIT License
# @author Fabrizzio Daniell Perilli Martín
# @email alu0101138589@ull.edu.es
#

from dash import Output, Input, callback
from layouts.alumno_layout import alumno_layout
from layouts.docente_layout import docente_layout
from layouts.gestor_layout import gestor_layout

@callback(
    Output('page-content', 'children'),
    Input('store-role', 'data')
)
def update_layout(role):
    """
    Actualiza el layout de la aplicación según el rol del usuario.

    Args:
        role (str): Rol del usuario

    Returns:
        str: Layout correspondiente al rol del usuario
        
    """
    if role == 'Alumno':
        return alumno_layout()
    elif role == 'Docente':
        return docente_layout()
    elif role == 'Gestor':
        return gestor_layout()
    return ""
