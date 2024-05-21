from dash import Input, Output, callback, State
from data.queries import gestores_all

@callback(
    Output('gestor-dropdown', 'value'),
    Output('gestor-dropdown', 'options'),
    Output('selected-gestor-store', 'data'),
    Input('gestor-dropdown', 'value'),
    State('selected-gestor-store', 'data'),
    State('gestor-dropdown', 'options')
)
def store_selected_gestor(selected_value, stored_value, dropdown_options):
    data = gestores_all()
    opciones_dropdown = [{'label': gestor[0], 'value': gestor[0]} for gestor in data]
    
    if selected_value is None and stored_value is not None:
        if stored_value in [option['value'] for option in opciones_dropdown]:
            return stored_value, opciones_dropdown, stored_value

    return selected_value, opciones_dropdown, selected_value