from dash import html, dcc
from callbacks.gestor.filters.callback_filter_all_curso_academico_gestor import update_filter_all_curso_academico_gestor


def filter_all_curso_academico_gestor():
    return html.Div([
        html.Label("Curso académico"),
        dcc.Dropdown(
            id="curso-all-academico-gestor",
            searchable=True,
            multi=True,
            clearable=False,
            options=[],
            value=None,    
            maxHeight=200,
            persistence=True,
            persistence_type='session',
        ),
        html.Button('Seleccionar todo', id='select-all-curso-academico-button', className='button-select-all-filter', n_clicks=0),
    ])