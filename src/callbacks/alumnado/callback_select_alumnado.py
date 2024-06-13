from dash import Input, Output, callback,State
from data.queries import alumnos_all

@callback(
    Output('alumnado-dropdown', 'value'),
    Output('alumnado-dropdown', 'options'),
    Output('selected-alumnado-store', 'data'),
    Input('alumnado-dropdown', 'value'),
    State('selected-alumnado-store', 'data'),
    State('alumnado-dropdown', 'options')
)
def store_selected_alumnado(selected_value, stored_value, dropdown_options):
    data = alumnos_all()
    opciones_dropdown = [{'label': alumno[0], 'value': alumno[0]} for alumno in data]
    
    if selected_value is None and stored_value is not None:
        if stored_value in [option['value'] for option in opciones_dropdown]:
            return stored_value, opciones_dropdown, stored_value

    return selected_value, opciones_dropdown, selected_value