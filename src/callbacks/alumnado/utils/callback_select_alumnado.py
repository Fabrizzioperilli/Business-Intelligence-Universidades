#
# @file callback_select_alumnado.py
# @brief Este fichero contiene el callback para almacenar el valor
#        seleccionado en el dropdown de alumnos
# @version 1.0
# @date 05/05/2024
# @license MIT License
# @author Fabrizzio Daniell Perilli Martín
# @email alu0101138589@ull.edu.es
#

from dash import Input, Output, State, callback
from data.queries import alumnos_all


@callback(
    Output("alumnado-dropdown", "value"),
    Output("alumnado-dropdown", "options"),
    Output("selected-alumnado-store", "data"),
    Input("alumnado-dropdown", "value"),
    State("selected-alumnado-store", "data"),
)
def store_selected_alumnado(selected_value, stored_value):
    """
    Almacena el valor seleccionado en el dropdown de alumnos.

    Args:
        selected_value (str): Valor seleccionado en el dropdown
        stored_value (str): Valor almacenado

    Returns:
        str: Valor seleccionado
        list: Opciones del dropdown
        str: Valor almacenado
    """
    data = alumnos_all()

    if not data:
        return None, [], None

    opciones_dropdown = [{"label": alumno[0], "value": alumno[0]} for alumno in data]

    if selected_value is None and stored_value in [
        op["value"] for op in opciones_dropdown
    ]:
        return stored_value, opciones_dropdown, stored_value

    return selected_value, opciones_dropdown, selected_value
