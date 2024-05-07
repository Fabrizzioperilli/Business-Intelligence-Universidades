from dash import Input, Output,callback
from data.db_connector import db


@callback(
  Output('asignaturas-matriculadas', 'options'),
  Output('asignaturas-matriculadas', 'value'),
  Input('selected-alumnado-store', 'data'),
  Input('curso-academico', 'value')
)
def update_filter_asignaturas_matri_alumnado(alumno_id, curso_academico):
    if not alumno_id or not curso_academico:
        return [], None
    
    if isinstance(curso_academico, str):
        curso_academico = (curso_academico,)
    else:
        curso_academico = tuple(curso_academico)

    query = """
    SELECT asignatura FROM asignaturas_matriculadas WHERE id = :id
    AND curso_aca IN :curso_academico
    """
    params = {'id': alumno_id, 'curso_academico': curso_academico}

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
    