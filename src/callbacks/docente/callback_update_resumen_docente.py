from dash import html, callback, Output, Input
from data.queries import resumen_docente
from callbacks.docente.callback_select_docente import store_selected_docente

@callback(
    Output('resumen-docente', 'children'),
    Input('selected-docente-store', 'data'),
    Input('titulacion-docente', 'value')
)
def update_resumen_docente(docente_id, titulacion):
    if not docente_id or not titulacion:
        return not_data()

    data = resumen_docente(docente_id, titulacion)

    if data:
        universidad = data[0][0]
        titulacion = data[0][1]
        id = data[0][2]
    else:
        return not_data()

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
