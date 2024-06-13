from dash import html
from callbacks.docente.callback_select_docente import store_selected_docente
from callbacks.docente.callback_update_resumen_docente import update_resumen_docente

def resumen_docente():
    return html.Div([
    ], id='resumen-docente')