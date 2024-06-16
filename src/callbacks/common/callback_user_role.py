from dash import Output, Input, State, callback


@callback(
    Output("dropdown_role", "value"),
    Input("store-role", "modified_timestamp"),
    State("store-role", "data"),
    prevent_initial_call=True,
)
def initialize_dropdown(ts, stored_role):
    """
    Inicializa el dropdown con el rol almacenado.
    
    Args:
    ts (float): Timestamp de la última modificación del store
    stored_role (str): Rol almacenado
    """
    return stored_role if ts is not None else "Alumno"


@callback(
    Output("store-role", "data"),
    Input("dropdown_role", "value"),
    State("store-role", "data"),
    prevent_initial_call=True,
)
def update_role(new_role, current_role):
    """
    Actualiza el rol almacenado en el store.
    
    Args:
    new_role (str): Nuevo rol seleccionado
    current_role (str): Rol actual almacenado
    
    Returns:
    str: Rol almacenado
    """
    if new_role != current_role:
        return new_role
    return current_role
