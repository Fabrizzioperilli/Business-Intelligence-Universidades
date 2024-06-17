from dash import Input, Output, callback, State
from data.queries import gestores_all


@callback(
    Output("gestor-dropdown", "value"),
    Output("gestor-dropdown", "options"),
    Output("selected-gestor-store", "data"),
    Input("gestor-dropdown", "value"),
    State("selected-gestor-store", "data"),
)
def store_selected_gestor(selected_value, stored_value):
    """
    Almacena el gestor seleccionado en un store.

    Args:
    selected_value (str): Valor seleccionado en el dropdown
    stored_value (dict): Datos almacenados en el store

    Returns:
    str: Valor seleccionado en el dropdown
    list: Opciones del dropdown
    str: Valor almacenado en el store
    """

    data = gestores_all()

    if not data:
        return None, [], None

    opciones_dropdown = [{"label": gestor[0], "value": gestor[0]} for gestor in data]

    if selected_value is None and stored_value in [
        op["value"] for op in opciones_dropdown
    ]:
        return stored_value, opciones_dropdown, stored_value

    return selected_value, opciones_dropdown, selected_value
