from dash import Input, Output, callback
from data.queries import cursos_academicos_egresados, universidades_gestor

@callback(
    Output('slider-curso-academico-gestor', 'marks'),
    Output('slider-curso-academico-gestor', 'max'),
    Output('slider-curso-academico-gestor', 'value'),
    Input('selected-gestor-store', 'data')
)
def update_slider(gestor_id):
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
    return marks, max_value, 1