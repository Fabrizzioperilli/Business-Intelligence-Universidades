from dash import Input, Output, State, callback, callback_context
from data.queries import asignaturas_actas_titulacion

@callback(
    Output('all-asignaturas-titulacion-docente', 'options'),
    Output('all-asignaturas-titulacion-docente', 'value'),
    Input('titulacion-docente', 'value'),
    Input('all-cursos-academicos-docente', 'value'),
    Input('select-all-asignaturas-titulacion-docente', 'n_clicks'),
    State('all-asignaturas-titulacion-docente', 'options')  # Cambiar el State aquí
)
def update_filter_asignaturas_docente(titulacion, curso_academico, n_clicks, existing_options):
    ctx = callback_context
    trigger_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if trigger_id == 'select-all-asignaturas-titulacion-docente':
        if existing_options and isinstance(existing_options, list):
            return existing_options, [option['value'] for option in existing_options]
        else:
            return [], []

    if not titulacion or not curso_academico:
        return [], None

    data = asignaturas_actas_titulacion(titulacion, curso_academico)
    
    if not data:
        return [], None

    opciones_dropdown = [{'label': asignatura[0], 'value': asignatura[0]} for asignatura in data]
    value = opciones_dropdown[0]['value'] if opciones_dropdown else None

    return opciones_dropdown, value