from dash import html, dcc
from callbacks.docente.filters.callback_filter_titulacion_docente import update_filter_titulacion_docente


def filter_titulacion_docente():
    """
    Crea un componente con un dropdown que contiene las titulaciones del perfil "Docente"
    en la pestaña "Rendimiento académico personal" y "Rendimiento académico general".

    Returns:
    html.Div: Componente con un dropdown
    """

    return html.Div(
        [
            html.Label("Titulación"),
            dcc.Dropdown(
                id="titulacion-docente",
                options=[],
                value=None,
                searchable=False,
                clearable=False,
                optionHeight=50,
                maxHeight=300,
            ),
            dcc.Store(id="selected-titulacion-docente-store", storage_type="local"),
        ]
    )
