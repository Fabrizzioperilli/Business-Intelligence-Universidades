from dash import html, dcc


def graphs_general_docente():
    return html.Div([
        html.Div([
            dcc.Graph(
                id='calificaiones-cuali-comparativa-asig-docente',
                figure={}
            )], className='graph-item-general-docente'),
    ], className='graphs-container-general-docente')