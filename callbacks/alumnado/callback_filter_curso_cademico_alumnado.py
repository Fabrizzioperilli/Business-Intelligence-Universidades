from dash import Input, Output, callback
from data.db_connector import db
from callbacks.alumnado.callback_select_alumnado import store_selected_alumnado

@callback(
    Output('curso-academico', 'options'),
    Output('curso-academico', 'value'),
    Input('selected-alumnado-store', 'data')
)
def update_filter_curso_academico_alumnado(alumno_id):
    if not alumno_id:
        return [], None

    query = "SELECT curso_aca FROM matricula WHERE id = :id"
    result = db.execute_query(query, {'id': alumno_id})
    opciones_dropdown = [{'label': curso[0], 'value': curso[0]} for curso in result]
    value = opciones_dropdown[0]['value'] if opciones_dropdown else None

    return opciones_dropdown, value

