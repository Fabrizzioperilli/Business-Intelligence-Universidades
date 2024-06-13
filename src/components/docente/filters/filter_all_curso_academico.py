from dash import html, dcc
from callbacks.docente.filters.callback_filter_all_curso_academico import update_filter_all_cursos_academicos_docente

def filter_all_curso_academico():
    return html.Div([
        html.Br(),
        html.Label("Curso académico"),
        dcc.Dropdown(
            id="all-cursos-academicos-docente",
            searchable=False,
            multi=False,
            clearable=False,
            options=[],
            value=None,    
            maxHeight=300,
        )
    ])