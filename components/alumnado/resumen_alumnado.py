from dash import html
from components.alumnado.select_alumnado import select_alumnado
from callbacks.docente.callback_update_resumen_docente import update_resumen_docente

def resumen_alumnado():
    return html.Div([
        html.H2("Resumen"),
        html.P(f"Universidad: "), 
        html.P(f"Titulación: "),
        html.P(f"Alumno: "),
        html.P(f"Nota Media: "),
        html.Hr(),
    ], id='resumen-alumnado')
    
