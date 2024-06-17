from dash import Input, Output, callback
from data.queries import curso_academico_actas_titulacion


@callback(
    Output("all-cursos-academicos-docente", "options"),
    Output("all-cursos-academicos-docente", "value"),
    Input("titulacion-docente", "value"),
)
def update_filter_all_cursos_academicos_docente(titulacion):
    """
    Actualiza las opciones del dropdown con todos los cursos académicos de la titulación seleccionada.
    
    Args:
    titulacion (str): Titulación seleccionada
    
    Returns:
    list: Opciones del dropdown
    list: Valor seleccionado
    """

    if not titulacion:
        return [], None

    data = curso_academico_actas_titulacion(titulacion)

    if not data:
        return [], None

    opciones_dropdown = [{"label": curso[0], "value": curso[0]} for curso in data]
    value = opciones_dropdown[0]["value"] if opciones_dropdown else None

    return opciones_dropdown, value
