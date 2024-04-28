
from dash import html, callback, Output, Input
import components.alumnado.tabs_alumnado as tabs_alumnado

# Define layout functions for each role
def alumno_layout():
    return html.Div([
        tabs_alumnado.tabs_alumnado(),
        html.H2("Alumno Dashboard", className='dashboard-title'),
    ])
    
    
@callback(Output('tabs-alumnado-content', 'children'),
            [Input('tabs-alumnado', 'value')])
def render_content(tab):
    if tab == 'expediente-personal-tab':
        return html.Div([
            html.H3("Expediente Académico Personal")
        ])
    elif tab == 'rendimiento-academico-tab':
        return html.Div([
            html.H3("Rendimiento Académico")
        ])
    else:
        return html.Div([
            html.H3("Expediente Académico Personal")
        ])