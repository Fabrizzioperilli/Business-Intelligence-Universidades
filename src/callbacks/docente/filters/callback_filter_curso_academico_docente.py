from dash import Input, Output, callback, State, callback_context
from data.queries import curso_academico_docente
from callbacks.docente.utils.callback_select_docente import store_selected_docente

@callback(
    Output('curso-academico-docente', 'options'),
    Output('curso-academico-docente', 'value'),
    Input('selected-docente-store', 'data'),
    Input('asignaturas-docente', 'value'),
    Input('select-all-cursos-academicos-docente', 'n_clicks'),
    State('curso-academico-docente', 'options')
)
def update_filter_curso_academico_docente(docente_id, asignatura, n_clicks, existing_options):
    ctx = callback_context
    trigger_id = ctx.triggered[0]['prop_id'].split('.')[0] if ctx.triggered else None

    if trigger_id == 'select-all-cursos-academicos' and n_clicks > 0:
            return existing_options, [option['value'] for option in existing_options]

    if not (docente_id and asignatura):
        return [], None
    
    data = curso_academico_docente(docente_id, asignatura)

    if not data:
        return [], None

    opciones_dropdown = [{'label': curso[0], 'value': curso[0]} for curso in data]
    value = [option['value'] for option in opciones_dropdown]
    
    return opciones_dropdown, value
