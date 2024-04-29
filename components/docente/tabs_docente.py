from dash import html, dcc

def tabs_docente():
    return html.Div([
        dcc.Tabs(id='tabs-docente', value='rendimiento-academico-asignatura-tab', children=[
            dcc.Tab(label='Rendimiento académico por asignatura', value='rendimiento-academico-asignatura-tab'),
            dcc.Tab(label='Rendimiento Académico', value='rendimiento-academico-tab'),
        ], className='tabs'),
        html.Div(id='tabs-docente-content'),
    ])