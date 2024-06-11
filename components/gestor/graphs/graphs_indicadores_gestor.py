from dash import html, dcc
from callbacks.gestor.graphs.indicadores.callback_graph_nuevo_ingreso_genero_gestor import update_graph_gestor
from callbacks.gestor.graphs.indicadores.callback_graph_egresados_genero_gestor import update_graph_gestor
from callbacks.gestor.graphs.indicadores.callback_graph_nuevo_ingreso_nacionalidad_gestor import update_graph_gestor
from callbacks.gestor.graphs.indicadores.callback_graph_egresados_nacionalidad_gestor import update_graph_gestor
from components.common.modal_data import create_modal
def graphs_indicadores_gestor():
    return html.Div([
        html.Div([
            dcc.Loading(
                children=[
                    dcc.Graph(
                        id='nuevo-ingreso-genero-gestor',
                        figure={},
                    )
                ]
            ),
            create_modal('modal-nuevo-ingreso-genero', 
                         'table-container-nuevo-ingreso-genero', 
                         'btn-descargar-nuevo-ingreso-genero', 
                         'btn-ver-datos-nuevo-ingreso-genero'),
        ], className='graph-item-indicadores-gestor'),
        
        html.Div([
            dcc.Loading(
                children=[
                    dcc.Graph(
                        id='nuevo_ingreso_nacionalidad-gestor',
                        figure={},
                    )
                ]
            ),
            create_modal('modal-nuevo-ingreso-nacionalidad', 
                         'table-container-nuevo-ingreso-nacionalidad', 
                         'btn-descargar-nuevo-ingreso-nacionalidad', 
                         'btn-ver-datos-nuevo-ingreso-nacionalidad'),
        ], className='graph-item-indicadores-gestor'),
        
        html.Div([
            dcc.Loading(
                children=[
                    dcc.Graph(
                        id='egresados-genero-gestor',
                        figure={}
                    )
                ]
            ),
            create_modal('modal-egresados-genero', 
                         'table-container-egresados-genero', 
                         'btn-descargar-egresados-genero', 
                         'btn-ver-datos-egresados-genero')
        ], className='graph-item-indicadores-gestor'),
        
        html.Div([
            dcc.Loading(
                children=[
                    dcc.Graph(
                        id='egresados-nacionalidad-gestor',
                        figure={}
                    )
                ]
            ),
            create_modal('modal-egresados-nacionalidad', 
                         'table-container-egresados-nacionalidad', 
                         'btn-descargar-egresados-nacionalidad', 
                         'btn-ver-datos-egresados-nacionalidad')
        ], className='graph-item-indicadores-gestor')
    ], className='graphs-container-indicadores-gestor')