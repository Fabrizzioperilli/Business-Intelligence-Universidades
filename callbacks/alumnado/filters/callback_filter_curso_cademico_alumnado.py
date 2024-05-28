from dash import Input, Output, callback, State, callback_context
from callbacks.alumnado.callback_select_alumnado import store_selected_alumnado
from data.queries import curso_academico_alumnado

@callback(
    Output('curso-academico', 'options'),
    Output('curso-academico', 'value'),
    Input('selected-alumnado-store', 'data'),
    Input('titulacion-alumnado', 'value'),
    Input('select-all-cursos-academicos', 'n_clicks'),
    State('curso-academico', 'options'),
    State('select-all-cursos-academicos', 'n_clicks_timestamp')  # Añadido para revisar cuándo fue clickeado
)
def update_filter_curso_academico_alumnado(alumno_id, titulacion, n_clicks, existing_options, last_clicked):
    ctx = callback_context
    trigger_id = ctx.triggered[0]['prop_id'].split('.')[0]

    #Evento de selección de todos los cursos académicos
    if trigger_id == 'select-all-cursos-academicos':
        if existing_options:
            return existing_options, [option['value'] for option in existing_options]
        else:
            return [], []

    if not alumno_id or not titulacion:
        return [], []
    
    result = curso_academico_alumnado(alumno_id, titulacion)        
    opciones_dropdown = [{'label': curso[0], 'value': curso[0]} for curso in result]
    value = [option['value'] for option in opciones_dropdown] if opciones_dropdown else []

    return opciones_dropdown, value


    