from dash import html
from callbacks.docente.callback_select_docente import store_selected_docente

def resumen_docente():
    return html.Div([
        html.H2("Resumen"),
        html.P(f"Universidad: "), 
        html.P(f"Titulación: "),
        html.P(f"Docente: "),
        html.Hr(),
    ], id='resumen-docente')