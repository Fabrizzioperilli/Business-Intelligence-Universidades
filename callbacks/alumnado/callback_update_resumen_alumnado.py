from dash import html, callback, Output, Input
from data.db_connector import db
from callbacks.alumnado.callback_select_alumnado import store_selected_alumnado
from utils.utils import calculate_average_grade

@callback(
    Output('resumen-alumnado', 'children'),
    [Input('selected-alumnado-store', 'data')]
)
def update_resumen_alumnado(alumno_id):
    if not alumno_id:
        return html.Div([
            html.H2("Resumen"),
            html.P("Universidad: No disponible"), 
            html.P("Titulación: No disponible"),
            html.P("Alumno: No disponible"),
            html.P("Nota Media: No disponible"),
            html.Hr(),
        ])

    query = "SELECT DISTINCT universidad, titulacion, id FROM matricula WHERE id = :id"
    result = db.execute_query(query, {'id': alumno_id})

    if result:
        universidad = result[0][0]
        titulacion = result[0][1]
        id = result[0][2]
    else:
        universidad = titulacion = id = "No disponible"

    return html.Div([
        html.H2("Resumen"),
        html.P("Universidad:", className="resumen-label"),
        html.P(universidad),
        html.P("Titulación:", className="resumen-label"),
        html.P(titulacion),
        html.P("Alumno:", className="resumen-label"),
        html.P(id),
        html.P("Nota Media:", className="resumen-label"),
        html.P(calculate_average_grade(alumno_id)),
        html.Hr(),
    ])
