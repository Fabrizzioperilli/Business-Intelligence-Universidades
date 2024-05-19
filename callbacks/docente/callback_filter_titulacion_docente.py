from dash import Input, Output, callback
from data.db_connector import db

@callback(
  Output('titulacion-docente', 'options'),
  Output('titulacion-docente', 'value'),
  Input('selected-docente-store', 'data'),
)
def update_filter_titulacion_docente(docente_id):
    if not docente_id:
        return [], None
    
    query = """
    SELECT DISTINCT titulacion FROM docentes WHERE id_docente = :docente_id
    """

    params = {'docente_id': docente_id}

    try:
        data = db.execute_query(query, params)
    except Exception as e:
        print("Query execution failed:", e)
        return [], None
    
    if not data:
        return [], None
    
    opciones_dropdown = [{'label': asignatura[0], 'value': asignatura[0]} for asignatura in data]
    value = opciones_dropdown[0]['value'] if opciones_dropdown else None
    
    return opciones_dropdown, value