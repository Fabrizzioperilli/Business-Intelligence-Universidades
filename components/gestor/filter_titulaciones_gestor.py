from dash import html, dcc
from callbacks.gestor.callback_filter_titulaciones_gestor import update_filter_titulaciones_gestor

def filter_titulaciones_gestor():
    return html.Div([
        html.Br(),
        html.Label("Titulaciones"),
        dcc.Dropdown(
            id="titulaciones-gestor",
            searchable=True,
            multi=True,
            clearable=False,
            options=[],
            value=None,    
            maxHeight=200,
            persistence=True,
            persistence_type='session',
        ),
        html.Button('Seleccionar todo', id='select-all-titulaciones-gestor', className='button-select-all-filter', n_clicks=0)
    ])