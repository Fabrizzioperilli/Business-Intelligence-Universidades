from dash import Input, Output, callback, State, callback_context
from callbacks.alumnado.callback_select_alumnado import store_selected_alumnado
from data.queries import curso_academico_alumnado

@callback(
    Output('curso-academico', 'options'),
    Output('curso-academico', 'value'),
    Input('selected-alumnado-store', 'data'),
    Input('titulacion-alumnado', 'value'),
    Input('select-all-cursos-academicos', 'n_clicks'),
    State('curso-academico', 'options')
)
def update_filter_curso_academico_alumnado(alumno_id, titulacion, n_clicks, existing_options):
    ctx = callback_context
    trigger_id = ctx.triggered[0]['prop_id'].split('.')[0] if ctx.triggered else None

    # Evento de selección de todos los cursos académicos
    if trigger_id == 'select-all-cursos-academicos' and n_clicks > 0:
        return existing_options, [option['value'] for option in existing_options]

    if not (alumno_id and titulacion):
        return [], None

    # Obtener los cursos académicos desde la base de datos
    data = curso_academico_alumnado(alumno_id, titulacion)

    if not data:
        return [], None

    opciones_dropdown = [{'label': curso[0], 'value': curso[0]} for curso in data]
    value = [option['value'] for option in opciones_dropdown]

    return opciones_dropdown, value


    