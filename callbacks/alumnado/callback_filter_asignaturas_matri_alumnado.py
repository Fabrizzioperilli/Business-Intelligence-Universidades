from dash import Input, Output, State, callback, callback_context
from data.db_connector import db
from utils.utils import list_to_tuple
from data.queries import asignaturas_matriculadas

@callback(
    Output('asignaturas-matriculadas', 'options'),
    Output('asignaturas-matriculadas', 'value'),
    Input('selected-alumnado-store', 'data'),
    Input('curso-academico', 'value'),
    Input('titulacion-alumnado', 'value'),
    Input('select-all-button', 'n_clicks'),
    State('asignaturas-matriculadas', 'options')
)
def update_filter_asignaturas_matri_alumnado(alumno_id, curso_academico, titulacion, n_clicks, existing_options):
    ctx = callback_context

    if not ctx.triggered:
        return [], None
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if button_id == 'select-all-button' and n_clicks > 0:
        return existing_options, [option['value'] for option in existing_options]

    if not alumno_id or not curso_academico or not titulacion:
        return [], None
    
    try:
        curso_academico = list_to_tuple(curso_academico)
    except Exception as e:
        return [], None

    data = asignaturas_matriculadas(alumno_id, curso_academico, titulacion)
    
    if not data:
        return [], None
    
    opciones_dropdown = [{'label': asignatura[0], 'value': asignatura[0]} for asignatura in data]
    return opciones_dropdown, opciones_dropdown[0]['value'] if opciones_dropdown else None
