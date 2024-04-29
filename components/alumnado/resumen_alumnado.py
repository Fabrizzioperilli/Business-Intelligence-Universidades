from dash import html

def resumen_alumnado():
    return html.Div([
            html.H2("Resumen"),
            html.P("Universidad: XXX"),
            html.P("Titulación: XXX"),
            html.P("Alumno: XXX"),
            html.P("Expediente: XXX"),
            html.P("Nota Media: XXX"),
            html.P("Estado: XXX"),
            html.Hr(),
    ])