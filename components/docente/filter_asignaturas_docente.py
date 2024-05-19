from dash import html, dcc
from callbacks.docente.callback_filter_asignaturas_docente import update_filter_asignaturas_docente


def filter_asignaturas_docente():
    return html.Div([
        html.Br(),
        html.Label("Asignaturas"),
        dcc.Dropdown(
            id="asignaturas-docente",
            searchable=True,
            value=None,
            clearable=True,
            options=[],
            maxHeight=300,
            optionHeight=50,
            persistence=True,
            persistence_type='local',
        )
    ])