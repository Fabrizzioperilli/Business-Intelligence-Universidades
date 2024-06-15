from dash import html
from callbacks.docente.graphs.general.callback_graph_all_calif_cualitativa_docente import update_graph_docente
from callbacks.docente.graphs.general.callback_graph_all_calif_media_docente import update_graph_docente
from components.common.create_graph import create_graph
from utils.utils import config_mode_bar_buttons_gestor

def graphs_general_docente():
    graphs_ids = [
        'calificaiones-cuali-all-asig-docente',
        'calificaiones-media-all-asig-docente'
    ]

    item_class = 'graph-item-general-docente'
    config = config_mode_bar_buttons_gestor

    return html.Div(
        [create_graph(graph_id, item_class, config) for graph_id in graphs_ids],
        className='graphs-container-general-docente'
    )
