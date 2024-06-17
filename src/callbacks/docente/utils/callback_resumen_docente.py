from dash import html, callback, Output, Input
from data.queries import universidades_docente


@callback(
    Output("resumen-docente", "children"),
    Input("selected-docente-store", "data"),
    Input("titulacion-docente", "value"),
)
def update_resumen_docente(docente_id, titulacion):
    """
    Actualiza el resumen del docente
    
    Args:
    docente_id (str): ID del docente
    titulacion (str): Titulación seleccionada
    
    Returns:
    html.Div: Layout del resumen del docente
    """
    if not (docente_id and titulacion):
        return not_data()

    data = universidades_docente(docente_id)

    if not data:
        return not_data()

    return html.Div(
        [
            html.H2("Resumen"),
            html.P("Universidad:", className="resumen-label"),
            html.P(data[0][1]),
            html.P("Titulación:", className="resumen-label"),
            html.P(titulacion),
            html.P("Docente:", className="resumen-label"),
            html.P(docente_id),
            html.Hr(),
        ]
    )


def not_data():
    return html.Div(
        [
            html.H2("Resumen"),
            html.P("Universidad:", className="resumen-label"),
            html.P("No disponible"),
            html.P("Titulación:", className="resumen-label"),
            html.P("No disponible"),
            html.P("Docente:", className="resumen-label"),
            html.P("No disponible"),
            html.Hr(),
        ]
    )
