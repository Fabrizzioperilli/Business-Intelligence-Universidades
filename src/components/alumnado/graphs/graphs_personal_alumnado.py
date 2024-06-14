from dash import html, dcc
from callbacks.alumnado.graphs.personal.callback_graph_calif_cualitativa_alumnado import update_graph_alumnado
from callbacks.alumnado.graphs.personal.callback_graph_progreso_academico_alumnado import update_graph_alumnado
from callbacks.alumnado.graphs.personal.callback_graph_calif_numerica_alumnado import update_graph_alumnado
from callbacks.alumnado.graphs.personal.callback_graph_tasa_rendimiento_alumnado import update_graph_alumnado
from components.common.create_graph import create_graph

def graphs_personal_alumnado():
    graph_ids = [
        'graph-evolucion-progreso-academico',
        'graph-bar-evolucion-asignaturas-matriculadas',
        'graph-bar-calificaciones-por-asignatura',
        'graph-bar-tasa-rendimiento'
    ]

    config={'displayModeBar': False}
    item_class = 'graph-item-personal-alumnado'
    
    return html.Div(
        [create_graph(graph_id, item_class, config) for graph_id in graph_ids],
        className='graphs-container-personal-alumnado'
    )
