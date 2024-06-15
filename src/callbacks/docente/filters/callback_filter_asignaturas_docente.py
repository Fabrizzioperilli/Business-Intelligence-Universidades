from dash import Input, Output, callback
from data.queries import asignaturas_docente

@callback(
    Output('asignaturas-docente', 'options'),
    Output('asignaturas-docente', 'value'),
    Input('selected-docente-store', 'data'),
    Input('titulacion-docente', 'value')
)
def update_filter_asignaturas_docente(docente_id, titulacion):
   
    if not (docente_id and titulacion):
        return [], None
     
    data = asignaturas_docente(docente_id, titulacion)
    
    if not data:
        return [], None
    
    opciones_dropdown = [{'label': asignatura[0], 'value': asignatura[0]} for asignatura in data]
    value = opciones_dropdown[0]['value'] if opciones_dropdown else None
    
    return opciones_dropdown, value