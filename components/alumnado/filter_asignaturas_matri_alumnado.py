from dash import html, dcc
from callbacks.alumnado.callback_filter_asignaturas_matri_alumnado import update_filter_asignaturas_matri_alumnado

def filter_asignaturas_matri_alumnado():
   return html.Div([
        html.Label("Asignaturas Matriculadas"),
        dcc.Dropdown(
            id="asignaturas-matriculadas",
            searchable=False,
            multi=True,
            clearable=False,
            options=[],
            value=None,
        ),
    ])
   