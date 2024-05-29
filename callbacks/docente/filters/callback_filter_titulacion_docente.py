from dash import Input, Output, State, callback
from data.queries import titulacion_docente

@callback(
  Output('titulacion-docente', 'options'),
  Output('titulacion-docente', 'value'),
  Output('selected-titulacion-docente-store', 'data'),
  Input('selected-docente-store', 'data'),
  Input('titulacion-docente', 'value'),
  State('selected-titulacion-docente-store', 'data')
)
def update_filter_titulacion_docente(docente_id, selected_value, stored_titulacion):
    if not docente_id:
        return [], None
    
    data = titulacion_docente(docente_id)
    
    if not data:
        return [], None
    
    opciones_dropdown = [{'label': asignatura[0], 'value': asignatura[0]} for asignatura in data]

    if selected_value is None and stored_titulacion:
        if stored_titulacion in [op['value'] for op in opciones_dropdown]:
            return opciones_dropdown, stored_titulacion, stored_titulacion
        
    return opciones_dropdown, selected_value, selected_value

    