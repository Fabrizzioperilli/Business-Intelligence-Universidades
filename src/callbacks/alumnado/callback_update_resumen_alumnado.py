from dash import html, callback, Output, Input
from data.queries import nota_media_alumno_titulacion, universidad_alumno

@callback(
    Output('resumen-alumnado', 'children'),
    Input('selected-alumnado-store', 'data'),
    Input('titulacion-alumnado', 'value')
)
def update_resumen_alumnado(alumno_id, titulacion):
    if not (alumno_id and titulacion):
        return not_data()
    
    universidad = universidad_alumno(alumno_id)

    if not universidad:
        return not_data()
    
    return html.Div([
        html.H2("Resumen"),
        html.P("Universidad:", className="resumen-label"),
        html.P(universidad[0][1]),
        html.P("Titulación:", className="resumen-label"),
        html.P(titulacion),
        html.P("Alumno:", className="resumen-label"),
        html.P(alumno_id),
        html.P("Nota Media:", className="resumen-label"),
        html.P(nota_media_alumno_titulacion(alumno_id, titulacion)),
        html.Hr(),
    ])


def not_data():
    return html.Div([
            html.H2("Resumen"),
            html.P("Universidad", className="resumen-label"),
            html.P("No disponible"), 
            html.P("Titulación", className="resumen-label"),
            html.P("No disponible"),
            html.P("Alumno", className="resumen-label"),
            html.P("No disponible"),
            html.P("Nota Media", className="resumen-label"),
            html.P("No disponible"),
            html.Hr(),
        ])
