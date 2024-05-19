from dash import html, callback, Output, Input
from data.db_connector import db
from callbacks.docente.callback_select_docente import store_selected_docente

@callback(
    Output('resumen-docente', 'children'),
    Input('selected-docente-store', 'data'),
    Input('titulacion-docente', 'value')
)
def update_resumen_docente(docente_id, titulacion):
    if not docente_id or not titulacion:
        return not_data()

    query = """
    SELECT DISTINCT universidad, titulacion, id_docente 
    FROM docentes 
    WHERE id_docente = :docente_id AND titulacion = :titulacion;
    """
    params = {'docente_id': docente_id, 'titulacion': titulacion}

    try:
        data = db.execute_query(query, params)
    except Exception as e:
        print("Query execution failed:", e)
        return not_data()

    if not data:
        return not_data()

    if data:
        universidad = data[0][0]
        titulacion = data[0][1]
        id = data[0][2]
    else:
        universidad = titulacion = id = "No disponible"

    return html.Div([
        html.H2("Resumen"),
        html.P("Universidad:", className="resumen-label"),
        html.P(universidad),
        html.P("Titulación:", className="resumen-label"),
        html.P(titulacion),
        html.P("Docente:", className="resumen-label"),
        html.P(id),
        html.Hr(),
    ])


def not_data():
    return html.Div([
            html.H2("Resumen"),
            html.P("Universidad: No disponible"), 
            html.P("Titulación: No disponible"),
            html.P("Docente: No disponible"),
            html.Hr(),
        ])
