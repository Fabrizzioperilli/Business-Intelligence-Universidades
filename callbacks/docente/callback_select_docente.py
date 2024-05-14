from dash import Input, Output, callback, State

@callback(
    Output('docente-dropdown', 'value'),
    Output('selected-docente-store', 'data'),
    Input('docente-dropdown', 'value'),
    State('selected-docente-store', 'data'),
    State('docente-dropdown', 'options')
)
def store_selected_docente(selected_value, stored_value, dropdown_options):
    if selected_value is None and stored_value is not None:
        available_values = [option['value'] for option in dropdown_options]
        if stored_value in available_values:
            return stored_value, stored_value
    return selected_value, selected_value