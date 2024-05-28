from dash import Input, Output, State, callback, callback_context
from data.queries import universidades_gestor, curso_academico_universidad

@callback(
    Output('curso-all-academico-gestor', 'options'),
    Output('curso-all-academico-gestor', 'value'),
    Input('selected-gestor-store', 'data'),
    Input('select-all-curso-academico-button', 'n_clicks'),
    State('curso-all-academico-gestor', 'options'),
    State('select-all-curso-academico-button', 'n_clicks_timestamp'),
)
def update_filter_all_curso_academico_gestor(gestor_id, n_clicks, existing_options, last_clicked):
    ctx = callback_context
    trigger_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if trigger_id == 'select-all-curso-academico-button':
        if existing_options:
            return existing_options, [option['value'] for option in existing_options]
        else:
            return [], []
        
    if not gestor_id:
        return [], None
    
    cod_universidad = universidades_gestor(gestor_id)
    if not cod_universidad:
        return [], None
    
    data = curso_academico_universidad(cod_universidad[0][0])

    if not data:
        return [], None
    
    opciones_dropdown = [{'label': curso[0], 'value': curso[0]} for curso in data]
    value = opciones_dropdown[0]['value'] if opciones_dropdown else None

    return opciones_dropdown, value