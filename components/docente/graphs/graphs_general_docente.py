from dash import html, dcc
from callbacks.docente.graphs.general.callback_graph_all_calif_cualitativa_docente import update_graph_docente
from callbacks.docente.graphs.general.callback_graph_all_calif_media_docente import update_graph_docente

def graphs_general_docente():
    return html.Div([
        html.Div([
            dcc.Graph(
                id='calificaiones-cuali-all-asig-docente',
                figure={}
            )], className='graph-item-general-docente'),
        html.Div([
            dcc.Graph(
                id='calificaiones-media-all-asig-docente',
                figure={}
            )], className='graph-item-general-docente'),
    ], className='graphs-container-general-docente')