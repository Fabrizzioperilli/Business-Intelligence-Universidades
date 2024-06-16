from dash import html
from callbacks.docente.graphs.personal.callback_graph_alu_repetidores_nuevos_docente import update_graph_docente
from callbacks.docente.graphs.personal.callback_graph_alu_genero_docente import update_graph_docente
from callbacks.docente.graphs.personal.callback_graph_alu_media_docente import update_graph_docente
from callbacks.docente.graphs.personal.callback_graph_alu_nota_cualitativa_docente import update_graph_docente
from components.common.create_graph import create_graph
from util import config_mode_bar_buttons_gestor

def graphs_personal_docente():
    graphs_ids = [
        'graph-alumnos-repetidores-nuevos',
        'graph-alumnos-matri-genero',
        'graph-alumnos-nota-media',
        'graph-alumnos-nota-cualitativa'
    ]

    item_class = 'graph-item-personal-docente'
    config = config_mode_bar_buttons_gestor

    return html.Div(
        [create_graph(graph_id, item_class, config) for graph_id in graphs_ids],
        className='graphs-container-personal-docente'
    )
