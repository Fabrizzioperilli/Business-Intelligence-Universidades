from dash import html, dcc

def tabs_gestor():
    return html.Div([
        dcc.Tabs(id='tabs-gestor', value='indicadores-academicos-tab', children=[
            dcc.Tab(label='Indicadores y resultados académicos', value='indicadores-academicos-tab'),
            dcc.Tab(label='Riesgo de abandono', value='riesgo-abandono-tab'),
        ], className='tabs'),
        html.Div(id='tabs-gestor-content'),
    ])