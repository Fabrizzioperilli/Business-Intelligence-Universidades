from dash import html, callback, Output, Input, State
from components.alumnado.sidebar_alumnado import toggle_button, sidebar_collapse_alumnado
from components.alumnado.graphs_alumnado import graphs_alumnado


@callback(Output('tabs-alumnado-content', 'children'),
            [Input('tabs-alumnado', 'value')])
def render_content(tab):
    if tab == 'expediente-personal-tab':
        return html.Div([
            toggle_button,
            sidebar_collapse_alumnado,
            html.Div(id='content', children=[
            html.H2("Dashboard Alumno", style={'textAlign': 'center'}),
                graphs_alumnado()
            ])
        ], style={'display': 'flex', 'flexDirection': 'row'})
    elif tab == 'rendimiento-academico-tab':
        return html.Div([
            html.H3("Rendimiento Académico")
        ])
    else:
        return html.Div([
            html.H3("Expediente Académico Personal")
        ])

@callback(
    Output('content', 'style'),
    [Input('sidebar-toggle', 'n_clicks')],
    [State('collapse', 'is_open')]
)
def toggle_graphs_layout(n, is_open):
    if not is_open:
        return {'width': '100%', 'transition': 'width 0.3s ease'}
    else:
        return {'width': '65%', 'transition': 'width 0.3s ease'}
        
        
    