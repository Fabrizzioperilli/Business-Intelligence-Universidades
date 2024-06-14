from dash import html, dcc
from callbacks.alumnado.graphs.general.callback_graph_calif_cual_comparativa import update_graph_alumnado
from callbacks.alumnado.graphs.general.callback_graph_calif_media_mi_nota import update_graph_alumnado
from callbacks.alumnado.graphs.general.callback_graph_asig_superadas_media import update_graph_alumnado
from components.common.create_graph import create_graph

def graphs_general_alumnado():
    graph_ids = [
        'asignaturas-superadas-general-mi-nota',
        'nota-cualitativa-general-mi-nota',
        'nota-media-general-mi-nota'
    ]
    
    config={'displayModeBar': False}
    item_class = 'graph-item-general-alumnado'

    return html.Div(
        [create_graph(graph_id, item_class, config) for graph_id in graph_ids],
        className='graphs-container-general-alumnado'
    )
