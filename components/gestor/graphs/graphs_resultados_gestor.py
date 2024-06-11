from dash import html, dcc
import dash_bootstrap_components as dbc
from callbacks.gestor.graphs.resultados.callback_graph_nota_acceso_titulacion_gestor import update_grpht_gestor
from callbacks.gestor.graphs.resultados.callback_graph_duracion_media_estudios_nota_gestor import update_graph_gestor
from components.common.modal_data import create_modal

def graphs_resultados_gestor():
    return html.Div([
        html.Div([
            dcc.Loading(
                children=[
                    dcc.Graph(
                        id='duración-estudios-nota-media-gestor',
                        figure={},
                    ),
                ]
            ),
            create_modal('modal-duracion-estudios', 
                         'table-container-duracion-estudios', 
                         'btn-descargar-csv-duracion-estudios', 
                         'btn-ver-datos-duracion-estudios')
        ], className='graph-item-resultados-gestor'),
        html.Div([
            dcc.Loading(
                children=[
                    dcc.Graph(
                        id='nota-acceso-titulacion',
                        figure={}
                    ),
                ]
            ),
            create_modal('modal-nota-acceso', 
                         'table-container-nota-acceso', 
                         'btn-descargar-csv-nota-acceso', 
                         'btn-ver-datos-nota-acceso')
        ], className='graph-item-resultados-gestor'),
    ], className='graphs-container-resultados-gestor')
