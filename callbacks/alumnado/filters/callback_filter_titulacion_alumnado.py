from dash import Input, Output, callback
from data.db_connector import db
from data.queries import titulacion_alumnado

@callback(
  Output('titulacion-alumnado', 'options'),
  Output('titulacion-alumnado', 'value'),
  Input('selected-alumnado-store', 'data')
)
def update_filter_titulacion_alumnado(alumno_id):
    if not alumno_id:
        return [], None
    
    data = titulacion_alumnado(alumno_id)
   
    if not data:
        return [], None
    
    opciones_dropdown = [{'label': asignatura[0], 'value': asignatura[0]} for asignatura in data]
    value = opciones_dropdown[0]['value'] if opciones_dropdown else None
    
    return opciones_dropdown, value
