from dash import html, callback, Output, Input
from data.queries import resumen_gestor, numero_alumnos_matriculados_universidad

@callback(
    Output('resumen-gestor', 'children'),
    Input('selected-gestor-store', 'data')
)
def update_resumen_gestor(gestor_id):
    if not gestor_id:
        return not_data()

    data = resumen_gestor(gestor_id)
    
    if data:
        universidad = data[0][0]
        id_gestor = data[0][1]
    else:
        return not_data()
    
    data_alumnos = numero_alumnos_matriculados_universidad(universidad)
    if data_alumnos:
        n_alumnos = data_alumnos[0][0]
    else:
        return not_data()
    
    return html.Div([
        html.H2("Resumen"),
        html.P("Universidad:", className="resumen-label"),
        html.P(universidad),
        html.P("Gestor:", className="resumen-label"),
        html.P(id_gestor),
        html.P("Número de alumnos matriculados:", className="resumen-label"),
        html.P(n_alumnos),
        html.Hr(),
    ])

def not_data():
    return html.Div([
            html.H2("Resumen"),
            html.P("Universidad: No disponible"), 
            html.P("Gestor: No disponible"),
            html.P("Número de alumnos matriculados: No disponible"),
            html.Hr(),
        ])