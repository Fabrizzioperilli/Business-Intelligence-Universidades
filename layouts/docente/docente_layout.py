from dash import html, callback, Output, Input
import components.docente.tabs_docente as tabs_docente

def docente_layout():
    return html.Div([
        tabs_docente.tabs_docente(),
        html.H2("Docente Dashboard", className='dashboard-title'),
        
    ])
    
@callback(Output('tabs-docente-content', 'children'),
            [Input('tabs-docente', 'value')])
def render_content(tab):
    if tab == 'rendimiento-academico-asignatura-tab':
        return html.Div([
            html.H3("Rendimiento académico por asignatura")
        ])
    elif tab == 'rendimiento-academico-tab':
        return html.Div([
            html.H3("Rendimiento Académico")
        ])
    else:
        return html.Div([
            html.H3("Rendimiento académico por asignatura")
        ])
    

