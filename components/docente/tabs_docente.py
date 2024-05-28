from dash import html, dcc
from callbacks.docente.callback_tabs_docente import render_content

def tabs_docente():
    return html.Div([
        dcc.Tabs(id='tabs-docente', value='rendimiento-academico-asignatura-tab', children=[
            dcc.Tab(label='Rendimiento académico personal', value='rendimiento-academico-asignatura-tab'),
            dcc.Tab(label='Rendimiento académico general', value='rendimiento-academico-tab'),
            dcc.Tab(label='Recomendaciones', value='recomendaciones-tab')
        ], className='tabs'),
        html.Div(id='tabs-docente-content'),
        dcc.Store(id='selected-docente-store', storage_type='local')
    ])