from dash import Input, Output, State, callback
from data.queries import universidades_gestor, curso_academico_universidad

@callback(
    Output('curso-academico-gestor', 'options'),
    Output('curso-academico-gestor', 'value'),
    Input('selected-gestor-store', 'data')
)
def update_filter_curso_academico_gestor(gestor_id):
    if not gestor_id:
        return [], None
    
    cod_universidad = universidades_gestor(gestor_id)
    if not cod_universidad:
        return [], None
    
    data = curso_academico_universidad(cod_universidad[0][0])

    if not data:
        return [], None
    
    opciones_dropdown = [{'label': curso[0], 'value': curso[0]} for curso in data]
    value = opciones_dropdown[0]['value'] if opciones_dropdown else None

    return opciones_dropdown, value