from dash import html, dcc
from callbacks.docente.utils.callback_select_docente import store_selected_docente

def select_docente():
    return html.Div([
        html.Div([
            dcc.Dropdown(
                options=[],
                value=None,
                id='docente-dropdown',
                clearable=False,
                placeholder='Selecciona un docente'
            )
        ], className='select-docente'),
    ]) 