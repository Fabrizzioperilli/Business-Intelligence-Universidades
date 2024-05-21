from dash import html, dcc
from callbacks.gestor.callback_tabs_gestor import render_content

def tabs_gestor():
    return html.Div([
        dcc.Tabs(id='tabs-gestor', value='indicadores-academicos-tab', children=[
            dcc.Tab(label='Indicadores académicos', value='indicadores-academicos-tab'),
            dcc.Tab(label='Resultados académicos', value='resultados-academicos-tab'),
            dcc.Tab(label='Riesgo de abandono', value='riesgo-abandono-tab'),
        ], className='tabs'),
        html.Div(id='tabs-gestor-content'),
        dcc.Store(id='selected-gestor-store', storage_type='local'),
        dcc.Location(id='url', refresh=False)
    ])