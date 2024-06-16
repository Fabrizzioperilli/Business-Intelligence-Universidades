from dash import html, callback, Output, Input
from data.queries import numero_alumnos_matriculados_universidad, universidades_gestor

@callback(
    Output('resumen-gestor', 'children'),
    Input('selected-gestor-store', 'data')
)
def update_resumen_gestor(gestor_id):
    if not gestor_id:
        return not_data()

    data = universidades_gestor(gestor_id)
    
    if not data:
        return not_data()
    
    data_alumnos = numero_alumnos_matriculados_universidad(data[0][1])

    if not data_alumnos:
        return not_data()
    
    return html.Div([
        html.H2("Resumen"),
        html.P("Universidad:", className="resumen-label"),
        html.P(data[0][1]),
        html.P("Gestor:", className="resumen-label"),
        html.P(gestor_id),
        html.P("Número de alumnos matriculados:", className="resumen-label"),
        html.P(data_alumnos[0][0]),
        html.Hr(),
    ])

def not_data():
    return html.Div([
            html.H2("Resumen"),
            html.P("Universidad:", className="resumen-label"),
            html.P("No disponible"), 
            html.P("Gestor:", className="resumen-label"),
            html.P("No disponible"),
            html.P("Número de alumnos matriculados:", className="resumen-label"),
            html.P("No disponible"),
            html.Hr(),
        ])