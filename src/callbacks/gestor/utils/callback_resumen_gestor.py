#
# @file callback_resumen_gestor.py
# @brief Este fichero contiene el callback para actualizar el resumen del gestor seleccionado.
# @version 1.0
# @date 21/05/2024
# @license MIT License
# @author Fabrizzio Daniell Perilli Martín
# @email alu0101138589@ull.edu.es
#

from dash import html, Output, Input, callback
from data.queries import numero_alumnos_matriculados_universidad, universidades_gestor


@callback(
        Output("resumen-gestor", "children"), 
        Input("selected-gestor-store", "data")
)
def update_resumen_gestor(gestor_id):
    """
    Actualiza el resumen del gestor seleccionado.
    
    Args:
        gestor_id (str): ID del gestor seleccionado
    
    Returns:
        html.Div: Resumen del gestor seleccionado
    """
    
    if not gestor_id:
        return not_data()

    data = universidades_gestor(gestor_id)

    if not data:
        return not_data()

    data_alumnos = numero_alumnos_matriculados_universidad(data[0][1])

    if not data_alumnos:
        return not_data()

    return html.Div(
        [
            html.H2("Resumen"),
            html.P("Universidad:", className="resumen-label"),
            html.P(data[0][1]),
            html.P("Gestor:", className="resumen-label"),
            html.P(gestor_id),
            html.P("Número de alumnos matriculados:", className="resumen-label"),
            html.P(data_alumnos[0][0]),
            html.Hr(),
        ]
    )


def not_data():
    return html.Div(
        [
            html.H2("Resumen"),
            html.P("Universidad:", className="resumen-label"),
            html.P("No disponible"),
            html.P("Gestor:", className="resumen-label"),
            html.P("No disponible"),
            html.P("Número de alumnos matriculados:", className="resumen-label"),
            html.P("No disponible"),
            html.Hr(),
        ]
    )
