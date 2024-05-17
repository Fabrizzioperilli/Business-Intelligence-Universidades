from dash import Input, Output, html, callback


@callback(Output('tabs-gestor-content', 'children'),
            [Input('tabs-gestor', 'value')])
def render_content(tab):
    if tab == 'indicadores-academicos-tab':
        return html.Div([
            html.H2("Dashboard Gestor", style={'textAlign': 'center'}),
            html.H3("Indicadores académicos")
        ])
    elif tab == 'resultados-academicos-tab':
        return html.Div([
            html.H2("Dashboard Gestor", style={'textAlign': 'center'}),
            html.H3("Resultados académicos")
        ])
    elif tab == 'riesgo-abandono-tab':
        return html.Div([
            html.H2("Dashboard Gestor", style={'textAlign': 'center'}),
            html.H3("Riesgo de abandono")
        ])
    else:
        return html.Div([
            html.H3("Indicadores académicos")
        ])


