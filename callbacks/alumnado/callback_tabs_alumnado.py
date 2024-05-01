from dash import html, callback, Output, Input, State
from components.alumnado.sidebar_alumnado import toggle_button, sidebar_collapse_alumnado
from components.alumnado.graphs_alumnado import graphs_alumnado


@callback(
    Output('tabs-alumnado-content', 'children'),
    [Input('tabs-alumnado', 'value')]
)
def render_content(tab):
    if tab == 'expediente-personal-tab':
        return html.Div([
            toggle_button,
            sidebar_collapse_alumnado,
            html.Div(id='content', children=[
                graphs_alumnado()
            ], style={'flex': 3})
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
    if is_open:
        return {'width': '75%', 'transition': 'width 0.5s ease'}
    else:
        return {'width': '100%', 'transition': 'width 0.5s ease'}