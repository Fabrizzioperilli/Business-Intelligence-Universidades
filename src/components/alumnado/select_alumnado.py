from dash import html, dcc
from callbacks.alumnado.callback_select_alumnado import store_selected_alumnado

def select_alumnado():
    return html.Div([
        html.Div([
            dcc.Dropdown(
                options=[],
                value=None,
                id='alumnado-dropdown',
                clearable=False
            )
        ], className='select-alumnado'),
    ]) 

