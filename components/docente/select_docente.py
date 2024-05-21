from dash import html, dcc
from callbacks.docente.callback_select_docente import store_selected_docente

def select_docente():
    return html.Div([
        html.Div([
            dcc.Dropdown(
                options=[],
                value=None,
                id='docente-dropdown',
                clearable=False
            )
        ], className='select-docente'),
    ]) 