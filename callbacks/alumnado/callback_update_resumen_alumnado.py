from dash import html, callback, Output, Input
from data.db_connector import db
from callbacks.alumnado.callback_select_alumnado import store_selected_alumnado
from utils.utils import calculate_average_grade
from data.queries import resumen_alumno

@callback(
    Output('resumen-alumnado', 'children'),
    Input('selected-alumnado-store', 'data'),
    Input('titulacion-alumnado', 'value')
)
def update_resumen_alumnado(alumno_id, titulacion):
    if not alumno_id:
        return html.Div([
            html.H2("Resumen"),
            html.P("Universidad: No disponible"), 
            html.P("Titulación: No disponible"),
            html.P("Alumno: No disponible"),
            html.P("Nota Media: No disponible"),
            html.Hr(),
        ])

    data = resumen_alumno(alumno_id, titulacion)
    
    #Comprobamos si hay datos
    if data:
        universidad = data[0][0]
        titulacion = data[0][1]
        id = data[0][2]
    else:
        universidad = "No disponible"
        titulacion = "No disponible"
        id = "No disponible"

    return html.Div([
        html.H2("Resumen"),
        html.P("Universidad:", className="resumen-label"),
        html.P(universidad),
        html.P("Titulación:", className="resumen-label"),
        html.P(titulacion),
        html.P("Alumno:", className="resumen-label"),
        html.P(id),
        html.P("Nota Media:", className="resumen-label"),
        html.P(calculate_average_grade(alumno_id, titulacion)),
        html.Hr(),
    ])
