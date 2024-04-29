from dash import html, callback, Output, Input
from components.alumnado.sidebar_alumnado import toggle_button, sidebar_collapse_alumnado


@callback(Output('tabs-alumnado-content', 'children'),
            [Input('tabs-alumnado', 'value')])
def render_content(tab):
    if tab == 'expediente-personal-tab':
        return html.Div([
            toggle_button,
            sidebar_collapse_alumnado
        ])
    elif tab == 'rendimiento-academico-tab':
        return html.Div([
            html.H3("Rendimiento Académico")
        ])
    else:
        return html.Div([
            html.H3("Expediente Académico Personal")
        ])