from dash import Input, Output, State, callback, callback_context
from data.db_connector import db
from utils.utils import list_to_tuple

@callback(
    Output('asignaturas-docente', 'options'),
    Output('asignaturas-docente', 'value'),
    Input('selected-docente-store', 'data'),
    Input('curso-academico-docente', 'value'),
    Input('select-all-button-asignaturas', 'n_clicks'),
    State('asignaturas-docente', 'options')
)
def update_filter_asignaturas_docente(docente_id, curso_academico, n_clicks, existing_options):
    ctx = callback_context

    if not ctx.triggered:
        return [], None
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if button_id == 'select-all-button-asignaturas' and n_clicks > 0:
        return existing_options, [option['value'] for option in existing_options]

    if not docente_id or not curso_academico:
        return [], None
    
    try:
        curso_academico = list_to_tuple(curso_academico)
    except Exception as e:
        return [], None

    query = """
    SELECT DISTINCT asignatura FROM docentes WHERE id_docente = :id_docente
    AND curso_aca IN :curso_academico
    """
    params = {'id_docente': docente_id, 'curso_academico': curso_academico}

    try:
        data = db.execute_query(query, params)
    except Exception as e:
        print("Query execution failed:", e)
        return [], None
    
    if not data:
        return [], None
    
    opciones_dropdown = [{'label': asignatura[0], 'value': asignatura[0]} for asignatura in data]
    return opciones_dropdown, opciones_dropdown[0]['value'] if opciones_dropdown else None