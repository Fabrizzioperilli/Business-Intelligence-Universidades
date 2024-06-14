from dash import Output, Input, State, callback

@callback(
    Output('dropdown_role', 'value'),
    Input('store-role', 'modified_timestamp'),
    State('store-role', 'data'),
    prevent_initial_call=True
)
def initialize_dropdown(ts, stored_role):
    return stored_role if ts is not None else 'Alumno'

@callback(
    Output('store-role', 'data'),
    Input('dropdown_role', 'value'),
    State('store-role', 'data'),
    prevent_initial_call=True
)
def update_role(new_role, current_role):
    if new_role != current_role:
        return new_role
    return current_role