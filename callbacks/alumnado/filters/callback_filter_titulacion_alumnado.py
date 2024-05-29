from dash import Input, Output, callback
from data.db_connector import db
from data.queries import titulacion_alumnado

from dash import Input, Output, callback, State
from data.db_connector import db
from data.queries import titulacion_alumnado

@callback(
    Output('titulacion-alumnado', 'options'),
    Output('titulacion-alumnado', 'value'),
    Output('selected-titulacion-alumnado-store', 'data'),
    Input('selected-alumnado-store', 'data'),
    Input('titulacion-alumnado', 'value'),
    State('selected-titulacion-alumnado-store', 'data')
)
def update_filter_titulacion_alumnado(alumno_id, selected_value, stored_titulacion):
    if not alumno_id:
        return [], None, None
    
    data = titulacion_alumnado(alumno_id)
    
    if not data:
        return [], None, None
    
    opciones_dropdown = [{'label': asignatura[0], 'value': asignatura[0]} for asignatura in data]
    
    if selected_value is None and stored_titulacion:
        if stored_titulacion in [op['value'] for op in opciones_dropdown]:
            return opciones_dropdown, stored_titulacion, stored_titulacion
    
    return opciones_dropdown, selected_value, selected_value
