from dash import html, dcc
from callbacks.alumnado.callback_filter_curso_cademico_alumnado import update_filter_curso_academico_alumnado

def filter_curso_academico_alumnado():
    return html.Div([
        html.Label("Curso Académico"),
        dcc.Dropdown(
            id="curso-academico",
            searchable=False,
            multi=True,
            clearable=False,
            options=[],
            value=None,
            persistence=True,
            persistence_type='local',
            maxHeight=300,
        ),
        html.Hr(),
    ])
