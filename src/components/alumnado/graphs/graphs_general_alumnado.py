from dash import html, dcc
from callbacks.alumnado.graphs.general.callback_graph_calif_cual_comparativa import update_graph_alumnado
from callbacks.alumnado.graphs.general.callback_graph_calif_media_mi_nota import update_graph_alumnado
from callbacks.alumnado.graphs.general.callback_graph_asig_superadas_media import update_graph_alumnado

def create_graph_div(graph_id):
    return html.Div([
        dcc.Loading(
            children=[
                dcc.Graph(
                    id=graph_id,
                    figure={},
                    config={'displayModeBar': False}
                )
            ]
        )
    ], className='graph-item-general-alumnado')

def graphs_general_alumnado():
    graph_ids = [
        'asignaturas-superadas-general-mi-nota',
        'nota-cualitativa-general-mi-nota',
        'nota-media-general-mi-nota'
    ]
    
    return html.Div(
        [create_graph_div(graph_id) for graph_id in graph_ids],
        className='graphs-container-general-alumnado'
    )
