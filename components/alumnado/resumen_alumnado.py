from dash import html
from components.alumnado.select_alumnado import select_alumnado
from callbacks.alumnado.callback_update_resumen_alumnado import update_resumen_alumnado

def resumen_alumnado():
    return html.Div([
        html.H2("Resumen"),
        html.P(f"Universidad: "), 
        html.P(f"Titulación: "),
        html.P(f"Alumno: "),
        html.P(f"Nota Media: "),
        html.Hr(),
        ], id='resumen-alumnado')
    
