from dash import Input, Output, callback, State
from data.queries import docentes_all


@callback(
    Output("docente-dropdown", "value"),
    Output("docente-dropdown", "options"),
    Output("selected-docente-store", "data"),
    Input("docente-dropdown", "value"),
    State("selected-docente-store", "data"),
)
def store_selected_docente(selected_value, stored_value):
    """
    Almacena el docente seleccionado en el store.

    Args:
    selected_value (str): Valor seleccionado
    stored_value (str): Valor almacenado

    Returns:
    str: Valor seleccionado
    list: Opciones del dropdown
    str: Valor almacenado
    """
    
    data = docentes_all()

    if not data:
        return None, [], None

    opciones_dropdown = [{"label": docente[0], "value": docente[0]} for docente in data]

    if selected_value is None and stored_value in [
        op["value"] for op in opciones_dropdown
    ]:
        return stored_value, opciones_dropdown, stored_value

    return selected_value, opciones_dropdown, selected_value
