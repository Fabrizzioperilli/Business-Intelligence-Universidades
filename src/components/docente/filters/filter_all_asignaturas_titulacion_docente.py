from dash import html, dcc
from callbacks.docente.filters.callback_filter_all_asignaturas_titulacion_docente import update_filter_asignaturas_docente


def filter_all_asignaturas_titulacion_docente():
    """
    Crea un componente con un dropdown que contiene todas las asignaturas de la titulación del perfil "Docente"
    en la pestaña "Rendimiento académico general".

    Returns:
    html.Div: Componente con un dropdown y un botón para seleccionar todas las asignaturas
    """
    return html.Div(
        [
            html.Br(),
            html.Label("Asignaturas"),
            dcc.Dropdown(
                id="all-asignaturas-titulacion-docente",
                searchable=True,
                value=None,
                clearable=True,
                options=[],
                maxHeight=300,
                optionHeight=50,
                persistence=True,
                persistence_type="local",
                multi=True,
            ),
            html.Button(
                "Seleccionar todo",
                id="select-all-asignaturas-titulacion-docente",
                className="button-select-all-filter",
                n_clicks=0,
            ),
        ]
    )
