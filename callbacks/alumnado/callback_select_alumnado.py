from dash import Input, Output, callback

@callback(
    Output('selected-alumnado-store', 'data'),
    [Input('alumnado-dropdown', 'value')]
)
def store_selected_alumnado(selected_alumnado):
    return selected_alumnado