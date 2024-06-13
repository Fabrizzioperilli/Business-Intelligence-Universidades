from dash import Output, Input, State, callback
        
@callback(
    Output("collapse", "is_open"),
    [Input("sidebar-toggle", "n_clicks")],
    [State("collapse", "is_open")],
)
def sidebar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open