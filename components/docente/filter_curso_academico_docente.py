from dash import html, dcc
from callbacks.docente.callback_filter_curso_academico_docente import update_filter_curso_academico_docente

def filter_curso_academico_docente():
    return html.Div([
        html.Br(),
        html.Label("Curso académico"),
        dcc.Dropdown(
            id="curso-academico-docente",
            searchable=False,
            multi=True,
            clearable=True,
            options=[],
            value=None,    
            maxHeight=300,
            persistence=True,
            persistence_type='session',
        ),
        html.Button('Seleccionar todo', id='select-all-cursos-academicos-docente', className='button-select-all-filter',n_clicks=0),
    ])
