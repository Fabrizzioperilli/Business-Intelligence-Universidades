from dash import Input, Output, callback
from data.queries import universidades_gestor, titulaciones_universidad_gestor

@callback(
  Output('titulaciones-gestor', 'options'),
  Output('titulaciones-gestor', 'value'),
  Input('selected-gestor-store', 'data'),
  Input('curso-academico-gestor', 'value')
)
def update_filter_titulaciones_gestor(docente_id, curso_academico):
    if not docente_id or not curso_academico:
        return [], None
    
    cod_universidad = universidades_gestor(docente_id)
    if not cod_universidad:
        return [], None
    
    data = titulaciones_universidad_gestor(cod_universidad[0][0], curso_academico) 
    
    if not data:
        return [], None
    
    opciones_dropdown = [{'label': asignatura[0], 'value': asignatura[0]} for asignatura in data]
    value = opciones_dropdown[0]['value'] if opciones_dropdown else None
    
    return opciones_dropdown, value