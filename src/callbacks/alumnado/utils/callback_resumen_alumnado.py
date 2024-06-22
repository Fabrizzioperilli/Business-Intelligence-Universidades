#
# @file callback_resumen_alumnado.py
# @brief Este fichero contiene el callback para actualizar el resumen del perfil "Alumno"
# @version 1.0
# @date 05/05/2024
# @license MIT License
# @author Fabrizzio Daniell Perilli Martín
# @email alu0101138589@ull.edu.es
#

from dash import html, callback, Output, Input
import pandas as pd
from data.queries import nota_media_alumno_titulacion, resumen_alumno
from util import load_model

@callback(
    Output("resumen-alumnado", "children"),
    Input("selected-alumnado-store", "data"),
    Input("titulacion-alumnado", "value"),
)
def update_resumen_alumnado(alumno_id, titulacion):
    """
    Actualiza el resumen del perfil "Alumno".

    Args:
        alumno_id (str): Identificador del alumno.
        titulacion (str): Titulación seleccionada

    Returns:
        list: Componentes con el resumen del perfil "Alumno"
    """
    if not (alumno_id and titulacion):
        return not_data()

    data = resumen_alumno(alumno_id, titulacion)

    data = pd.DataFrame(data, columns=["id_alumno", "universidad", "titulacion", "abandona"])
    
    if data.empty:
        return not_data()

    componentes = [
        html.H2("Resumen"),
        html.P("Universidad:", className="resumen-label"),
        html.P(data["universidad"].iloc[0]),
        html.P("Titulación:", className="resumen-label"),
        html.P(data["titulacion"].iloc[0]),
        html.P("Alumno:", className="resumen-label"),
        html.P(alumno_id),
        html.P("Nota Media:", className="resumen-label"),
        html.P(nota_media_alumno_titulacion(alumno_id, titulacion))
    ]

    if data["abandona"].iloc[0] == 'no':
        componentes.append(html.P("Estado:", className="resumen-label"))
        componentes.append(html.P("Activo"))
        componentes.append(html.P("Probabilidad de abandono:", className="resumen-label"))
        data_model = load_model()
        ## Obtener la probabilidad de abandono del modelo con el id_alumno
        probabilidad_abandono = data_model[data_model['id'] == alumno_id]['probabilidad_abandono'].values[0]
        componentes.append(html.P(f"{probabilidad_abandono:.2%}"))
    else:
        componentes.append(html.P("Estado:", className="resumen-label"))
        componentes.append(html.P("Abandona"))
        

    componentes.append(html.Hr())
    
    return html.Div(componentes)



def not_data():
    return html.Div(
        [
            html.H2("Resumen"),
            html.P("Universidad:", className="resumen-label"),
            html.P("No disponible"),
            html.P("Titulación:", className="resumen-label"),
            html.P("No disponible"),
            html.P("Alumno:", className="resumen-label"),
            html.P("No disponible"),
            html.P("Nota Media:", className="resumen-label"),
            html.P("No disponible"),
            html.Hr(),
        ]
    )
