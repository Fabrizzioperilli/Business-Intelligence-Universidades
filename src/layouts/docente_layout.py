from dash import html
import components.docente.utils.tabs_docente as tabs_docente

def docente_layout():
    return html.Div([
        tabs_docente.tabs_docente()  
    ])
    

