from dash import html, dcc
from callbacks.gestor.graphs.resultados.callback_graph_nota_acceso_titulacion_gestor import update_grpht_gestor
from callbacks.gestor.graphs.resultados.callback_graph_duracion_media_estudios_nota_gestor import update_graph_gestor
from callbacks.gestor.filters.callback_filter_curso_academico_slider_gestor import update_slider
from components.common.modal_data import create_modal

def graphs_resultados_gestor():
    return html.Div([
        html.Div([
            dcc.Graph(
                id='duración-estudios-nota-media-gestor',
                figure={},
            ),
            create_modal('modal-duracion-media',
                         'table-container-duracion-media', 
                         'btn-descargar-csv-duracion-media', 
                         'btn-ver-datos-duracion-media'),
            dcc.Slider(
                id='slider-curso-academico-gestor',
                step=1,
                marks={},
                value=1,
            )
        ], className='graph-item-resultados-gestor'),
        html.Div([
            dcc.Graph(
                id='nota-acceso-titulacion',
                figure={}
            ),
            create_modal('modal-nota-acceso', 
                         'table-container-nota-acceso', 
                         'btn-descargar-csv-nota-acceso', 
                         'btn-ver-datos-nota-acceso')
        ], className='graph-item-resultados-gestor'),
    ], className='graphs-container-resultados-gestor')
