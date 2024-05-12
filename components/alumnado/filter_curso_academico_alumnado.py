from dash import html, dcc
from callbacks.alumnado.callback_filter_curso_cademico_alumnado import update_filter_curso_academico_alumnado

def filter_curso_academico_alumnado():
    return html.Div([
        html.Label("Curso cadémico"),
        dcc.Dropdown(
            id="curso-academico",
            searchable=False,
            multi=True,
            clearable=True,
            options=[],
            value=None,    
            maxHeight=300,
            persistence=True,
            persistence_type='session',
        ),
        html.Button('Seleccionar todo', id='select-all-cursos-academicos', n_clicks=0),
        html.Hr(),
    ])
