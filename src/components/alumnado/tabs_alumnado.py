from dash import html, dcc
from callbacks.alumnado.callback_tabs_alumnado import render_content

def tabs_alumnado():
    return html.Div([
        dcc.Tabs(id='tabs-alumnado', value='expediente-personal-tab', children=[
            dcc.Tab(label='Expediente académico personal', value='expediente-personal-tab'),
            dcc.Tab(label='Rendimiento académico general', value='rendimiento-academico-tab'),
            dcc.Tab(label='Recomendaciones', value='recomendador-tab'),
        ], className='tabs' ),
        html.Div(id='tabs-alumnado-content'),
        dcc.Store(id='selected-alumnado-store', storage_type='local'),
        dcc.Location(id='url', refresh=False)
    ])