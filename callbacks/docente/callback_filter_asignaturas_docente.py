from dash import Input, Output, callback
from data.db_connector import db
from utils.utils import list_to_tuple

@callback(
    Output('asignaturas-docente', 'options'),
    Output('asignaturas-docente', 'value'),
    Input('selected-docente-store', 'data'),
  
)
def update_filter_asignaturas_docente(docente_id):
   
    if not docente_id:
        return [], None
     
    query = """
    SELECT DISTINCT asignatura FROM docentes WHERE id_docente = :id_docente
    """
    params = {'id_docente': docente_id}

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