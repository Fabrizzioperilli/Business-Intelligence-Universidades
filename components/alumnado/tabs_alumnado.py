from dash import html, dcc

def tabs_alumnado():
    return html.Div([
        dcc.Tabs(id='tabs-alumnado', value='expediente-personal-tab', children=[
            dcc.Tab(label='Expediente Académico Personal', value='expediente-personal-tab'),
            dcc.Tab(label='Rendimiento Académico', value='rendimiento-academico-tab'),
        ], className='tabs' ),
        html.Div(id='tabs-alumnado-content'),
    ])