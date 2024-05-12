from dash import html, dcc
from callbacks.alumnado.callback_filter_asignaturas_matri_alumnado import update_filter_asignaturas_matri_alumnado

def filter_asignaturas_matri_alumnado():
   return html.Div([
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
            persistence=True,
            persistence_type='local',
        ),
        html.Button('Seleccionar todo', id='select-all-button', n_clicks=0),
    ])
   