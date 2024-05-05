from dash import html, dcc
from callbacks.alumnado.callback_update_filters_alumnado import update_filters_alumnado

def filters_alumnado():
    return html.Div([
        html.H2("Filtros"),
        html.Label("Curso Académico"),
        dcc.Dropdown(
            id='curso-academico',
            searchable=False,
            clearable=False,
            options=[],
            value=None
        )
    ], className='filters')