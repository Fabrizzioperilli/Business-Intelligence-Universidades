from dash import Input, Output, State, callback, callback_context
from data.queries import universidades_gestor, titulaciones_universidad_gestor

@callback(
  Output('titulaciones-gestor', 'options'),
  Output('titulaciones-gestor', 'value'),
  Input('selected-gestor-store', 'data'),
  Input('curso-academico-gestor', 'value'),
  Input('select-all-titulaciones-gestor', 'n_clicks'),
  State('titulaciones-gestor', 'options'),
  State('select-all-titulaciones-gestor', 'n_clicks_timestamp')

)
def update_filter_titulaciones_gestor(docente_id, curso_academico, n_clicks, existing_options, last_clicked):
    ctx = callback_context
    trigger_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if trigger_id == 'select-all-titulaciones-gestor':
        if existing_options:
            return existing_options, [option['value'] for option in existing_options]
        else:
            return [], None

    if not docente_id or not curso_academico:
        return [], None
    
    cod_universidad = universidades_gestor(docente_id)
    if not cod_universidad:
        return [], None
    
    data = titulaciones_universidad_gestor(cod_universidad[0][0], curso_academico) 
    
    if not data:
        return [], None
    
    opciones_dropdown = [{'label': curso[0], 'value': curso[0]} for curso in data]
    value = [option['value'] for option in opciones_dropdown] if opciones_dropdown else []
    
    return opciones_dropdown, value