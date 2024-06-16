from dash import html, dcc
from callbacks.alumnado.filters.callback_filter_asignaturas_matri_alumnado import update_filter_asignaturas_matri_alumnado

def filter_asignaturas_matri_alumnado():
    return html.Div(
        [
            html.Br(),
            html.Label("Asignaturas matriculadas"),
            dcc.Dropdown(
                id="asignaturas-matriculadas",
                searchable=True,
                multi=True,
                value=None,
                clearable=True,
                options=[],
                maxHeight=300,
                optionHeight=50,
                placeholder="Seleccione una opción",
            ),
            html.Button(
                "Seleccionar todo",
                id="select-all-button",
                className="button-select-all-filter",
                n_clicks=0,
            ),
        ]
    )
