from dash import html, dcc
from callbacks.gestor.filters.callback_filter_curso_academico_gestor import update_filter_curso_academico_gestor

def filter_curso_academico_gestor():
    return html.Div([
        html.Label("Curso académico"),
        dcc.Dropdown(
            id="curso-academico-gestor",
            searchable=True,
            multi=False,
            clearable=False,
            options=[],
            value=None,    
            maxHeight=200,
            persistence=True,
            persistence_type='session',
        )
    ])