from dash import html, callback, Output, Input
import components.gestor.tabs_gestor as tabs_gestor

def gestor_layout():
    return html.Div([
        tabs_gestor.tabs_gestor(),
        html.H2("Gestor Dashboard", className='dashboard-title'),
    ])
    

@callback(Output('tabs-gestor-content', 'children'),
            [Input('tabs-gestor', 'value')])
def render_content(tab):
    if tab == 'indicadores-academicos-tab':
        return html.Div([
            html.H3("Indicadores y resultados académicos")
        ])
    elif tab == 'riesgo-abandono-tab':
        return html.Div([
            html.H3("Riesgo de abandono")
        ])
    else:
        return html.Div([
            html.H3("Indicadores y resultados académicos")
        ])
    
