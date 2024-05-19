from dash import Input, Output, callback
from data.db_connector import db

@callback(
  Output('titulacion-alumnado', 'options'),
  Output('titulacion-alumnado', 'value'),
  Input('selected-alumnado-store', 'data')
)
def update_filter_titulacion_alumnado(alumno_id):
    if not alumno_id:
        return [], None
    
    query = """
    SELECT DISTINCT titulacion FROM matricula WHERE id = :alumno_id
    """

    params = {'alumno_id': alumno_id}

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
