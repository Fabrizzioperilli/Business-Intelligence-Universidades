from dash import Input, Output, callback
from data.queries import titulacion_docente

@callback(
  Output('titulacion-docente', 'options'),
  Output('titulacion-docente', 'value'),
  Input('selected-docente-store', 'data'),
)
def update_filter_titulacion_docente(docente_id):
    if not docente_id:
        return [], None
    
    data = titulacion_docente(docente_id)
    
    if not data:
        return [], None
    
    opciones_dropdown = [{'label': asignatura[0], 'value': asignatura[0]} for asignatura in data]
    value = opciones_dropdown[0]['value'] if opciones_dropdown else None
    
    return opciones_dropdown, value