from dash import Input, Output, callback,State

@callback(
    Output('alumnado-dropdown', 'value'),
    Output('selected-alumnado-store', 'data'),
    Input('alumnado-dropdown', 'value'),
    State('selected-alumnado-store', 'data'),
    State('alumnado-dropdown', 'options')
)
def store_selected_alumnado(selected_value, stored_value, dropdown_options):
    if selected_value is None and stored_value is not None:
        available_values = [option['value'] for option in dropdown_options]
        if stored_value in available_values:
            return stored_value, stored_value
    return selected_value, selected_value