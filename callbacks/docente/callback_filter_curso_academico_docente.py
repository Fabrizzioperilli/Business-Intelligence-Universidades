from dash import Input, Output, callback, State, callback_context
from data.db_connector import db
from callbacks.docente.callback_select_docente import store_selected_docente

@callback(
    Output('curso-academico-docente', 'options'),
    Output('curso-academico-docente', 'value'),
    Input('selected-docente-store', 'data'),
    Input('asignaturas-docente', 'value'),
    Input('select-all-cursos-academicos-docente', 'n_clicks'),
    State('curso-academico-docente', 'options'),
    State('select-all-cursos-academicos-docente', 'n_clicks_timestamp')  # Añadido para revisar cuándo fue clickeado
)
def update_filter_curso_academico_docente(docente_id, asignatura, n_clicks, existing_options, last_clicked):
    ctx = callback_context
    trigger_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if trigger_id == 'select-all-cursos-academicos':
        if existing_options:
            return existing_options, [option['value'] for option in existing_options]
        else:
            return [], []

    if docente_id:
        query = """
        SELECT curso_aca 
        FROM docentes 
        WHERE id_docente = :id_docente AND asignatura = :asignatura;
        """
        params = {'id_docente': docente_id, 'asignatura': asignatura}

        try: 
            result = db.execute_query(query, params)
        except Exception as e:
            print("Query execution failed:", e)
            return [], []
      
        
        opciones_dropdown = [{'label': curso[0], 'value': curso[0]} for curso in result]
        return opciones_dropdown, [option['value'] for option in opciones_dropdown] if opciones_dropdown else []

    return [], []