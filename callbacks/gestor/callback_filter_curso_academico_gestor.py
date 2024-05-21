from dash import Input, Output, State, callback, callback_context
from data.queries import universidades_gestor, curso_academico_universidad

@callback(
    Output('curso-academico-gestor', 'options'),
    Output('curso-academico-gestor', 'value'),
    Input('selected-gestor-store', 'data'),
    Input('select-all-titulaciones-gestor', 'n_clicks'),
    State('curso-academico-gestor', 'options'),
    State('select-all-titulaciones-gestor', 'n_clicks_timestamp')
)
def update_filter_curso_academico_gestor(gestor_id, n_clicks, existing_options, last_clicked):
    ctx = callback_context
    trigger_id = ctx.triggered[0]['prop_id'].split('.')[0]

    #Evento de selección de todos los cursos académicos
    if trigger_id == 'select-all-cursos-academicos':
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