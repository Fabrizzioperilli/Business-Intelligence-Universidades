from dash import html, dcc
from callbacks.alumnado.graphs.personal.callback_graph_calif_cualitativa_alumnado import update_graph_alumnado
from callbacks.alumnado.graphs.personal.callback_graph_progreso_academico_alumnado import update_graph_alumnado
from callbacks.alumnado.graphs.personal.callback_graph_calif_numerica_alumnado import update_graph_alumnado
from callbacks.alumnado.graphs.personal.callback_graph_tasa_rendimiento_alumnado import update_graph_alumnado

def graphs_personal_alumnado():
    return html.Div([
        html.Div([
            dcc.Loading(
                children=[
                    dcc.Graph(
                        id='graph-evolucion-progreso-academico',
                        figure={},
                    )
                ]
            )
        ], className='graph-item-personal-alumnado'),
        
        html.Div([
            dcc.Loading(
                children=[
                    dcc.Graph(
                        id='graph-bar-evolucion-asignaturas-matriculadas',
                        figure={}
                    )
                ]
            )
        ], className='graph-item-personal-alumnado'),
        
        html.Div([
            dcc.Loading(
                children=[
                    dcc.Graph(
                        id='graph-bar-calificaciones-por-asignatura',
                        figure={},
                    )
                ]
            )
        ], className='graph-item-personal-alumnado'),
        
        html.Div([
            dcc.Loading(
                children=[
                    dcc.Graph(
                        id='graph-bar-tasa-rendimiento',
                        figure={}
                    )
                ]
            )
        ], className='graph-item-personal-alumnado')
    ], className='graphs-container-personal-alumnado')