from dash import html, dcc
from callbacks.alumnado.graphs.personal.callback_graph_calif_cualitativa_alumnado import update_graph_alumnado
from callbacks.alumnado.graphs.personal.callback_graph_progreso_academico_alumnado import update_graph_alumnado
from callbacks.alumnado.graphs.personal.callback_graph_calif_numerica_alumnado import update_graph_alumnado
from callbacks.alumnado.graphs.personal.callback_graph_tasa_rendimiento_alumnado import update_graph_alumnado


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
    ], className='graph-item-personal-alumnado')


def graphs_personal_alumnado():
    graph_ids = [
        'graph-evolucion-progreso-academico',
        'graph-bar-evolucion-asignaturas-matriculadas',
        'graph-bar-calificaciones-por-asignatura',
        'graph-bar-tasa-rendimiento'
    ]
    
    return html.Div(
        [create_graph_div(graph_id) for graph_id in graph_ids],
        className='graphs-container-personal-alumnado'
    )
