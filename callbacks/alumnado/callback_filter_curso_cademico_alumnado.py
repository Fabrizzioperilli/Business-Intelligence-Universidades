from dash import Input, Output, callback, State, callback_context
from data.db_connector import db
from callbacks.alumnado.callback_select_alumnado import store_selected_alumnado

@callback(
    Output('curso-academico', 'options'),
    Output('curso-academico', 'value'),
    Input('selected-alumnado-store', 'data'),
    Input('select-all-cursos-academicos', 'n_clicks'),
    State('curso-academico', 'options'),
    State('select-all-cursos-academicos', 'n_clicks_timestamp')  # Añadido para revisar cuándo fue clickeado
)
def update_filter_curso_academico_alumnado(alumno_id, n_clicks, existing_options, last_clicked):
    ctx = callback_context

    # Revisar qué disparó el callback
    trigger_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if trigger_id == 'select-all-cursos-academicos':
        # Seleccionar todo fue presionado
        if existing_options:
            return existing_options, [option['value'] for option in existing_options]
        else:
            return [], []

    if alumno_id:
        # Lógica para actualizar basada en alumno_id
        query = "SELECT curso_aca FROM matricula WHERE id = :id"
        result = db.execute_query(query, {'id': alumno_id})
        opciones_dropdown = [{'label': curso[0], 'value': curso[0]} for curso in result]
        return opciones_dropdown, [option['value'] for option in opciones_dropdown] if opciones_dropdown else []

    return [], []