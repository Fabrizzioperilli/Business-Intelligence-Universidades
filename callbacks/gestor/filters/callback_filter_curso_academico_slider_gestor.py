from dash import Input, Output, callback, State, callback_context
from data.queries import cursos_academicos_egresados, universidades_gestor

@callback(
    Output('slider-curso-academico-gestor', 'marks'),
    Output('slider-curso-academico-gestor', 'max'),
    Output('slider-curso-academico-gestor', 'value'),
    Input('selected-gestor-store', 'data'),
    Input('interval', 'n_intervals')
)
def update_slider(gestor_id, n_intervals):
    if not gestor_id:
        return {}, 1, 1
    
    data_universidad = universidades_gestor(gestor_id)
    if not data_universidad:
        return {}, 1, 1
    
    fechas_cursos = cursos_academicos_egresados(data_universidad[0][0])
    if not fechas_cursos:
        return {}, 1, 1
    
    marks = {i+1: str(fecha[0]) for i, fecha in enumerate(fechas_cursos)}
    max_value = len(fechas_cursos)
    
    # Si el intervalo está habilitado, incrementa el valor del slider
    if n_intervals is not None:
        current_value = (n_intervals % max_value) + 1
        return marks, max_value, current_value

    return marks, max_value, 1

@callback(
    Output('interval', 'disabled'),
    Input('play-button', 'n_clicks'),
    Input('pause-button', 'n_clicks'),
    State('interval', 'disabled')
)
def play_pause(play, pause, disabled):
    ctx = callback_context
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]
    
    if button_id == 'play-button':
        return False
    elif button_id == 'pause-button':
        return True
    
    return disabled