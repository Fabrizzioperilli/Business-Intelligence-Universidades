from dash import html, callback, Output, Input, State
from components.alumnado.sidebar_alumnado import toggle_button, sidebar_collapse_alumnado
from components.alumnado.graphs_alumnado import graphs_alumnado
from components.alumnado.select_alumnado import select_alumnado


@callback(
    Output('tabs-alumnado-content', 'children'),
    [Input('tabs-alumnado', 'value')],
    State('selected-alumnado-store', 'data') 
)
def render_content(tab, selected_alumnado):
    if tab == 'expediente-personal-tab':
        return html.Div([
            select_alumnado(),
            html.H2("Dashboard Alumnado", style={'textAlign': 'center'}),
            html.Div([
                toggle_button,
                sidebar_collapse_alumnado,
                graphs_alumnado(),
            ], className='content-layout-dashboard')
        ])
    elif tab == 'rendimiento-academico-tab':
        return html.Div([
            html.H2("Dashboard Alumnado", style={'textAlign': 'center'}),
            html.Div([
                toggle_button,
                sidebar_collapse_alumnado,
            ], className='content-layout-dashboard')
        ])
    elif tab == 'recomendador-tab':
        return html.Div([
            html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam nec purus nec elit lacinia fermentum. ")
        ])
    else:
        return html.Div([
            html.H3("Expediente Académico Personal")
        ])