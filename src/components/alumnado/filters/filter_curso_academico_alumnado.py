from dash import html, dcc
from callbacks.alumnado.filters.callback_filter_curso_cademico_alumnado import update_filter_curso_academico_alumnado

def filter_curso_academico_alumnado():
    return html.Div([
        html.Br(),
        html.Label("Curso académico"),
        dcc.Dropdown(
            id="curso-academico",
            searchable=False,
            multi=True,
            clearable=True,
            options=[],
            value=None,    
            maxHeight=300,
            placeholder="Seleccione una opción"
        ),
        html.Button('Seleccionar todo', id='select-all-cursos-academicos', className='button-select-all-filter', n_clicks=0)
    ])
