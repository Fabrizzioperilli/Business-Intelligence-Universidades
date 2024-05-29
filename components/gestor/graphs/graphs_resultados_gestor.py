from dash import html, dcc
import dash_bootstrap_components as dbc
from callbacks.gestor.graphs.resultados.callback_graph_nota_acceso_titulacion_gestor import update_grpht_gestor
from callbacks.gestor.graphs.resultados.callback_graph_duracion_media_estudios_nota_gestor import update_graph_gestor
from callbacks.gestor.filters.callback_filter_curso_academico_slider_gestor import update_slider

def graphs_resultados_gestor():
    return html.Div([
        html.Div([
            dcc.Graph(
                id='duración-estudios-nota-media-gestor',
                figure={},
            ),
            dbc.Modal([
                dbc.ModalHeader("Datos"),
                dbc.ModalBody(html.Div(id='table-container-1')),
                dbc.ModalFooter(
                    dbc.Button("Descargar CSV", id='btn-descargar-csv-1', color='primary')
                )
            ], id='modal-1', is_open=False, size="lg"),
            html.Label('Curso académico'),
            dcc.Slider(
                id='slider-curso-academico-gestor',
                step=1,
                marks={},
                value=1,
            ),
            dbc.Button('Ver datos', id='btn-ver-datos-1', n_clicks=0, color='primary')
        ], className='graph-item-resultados-gestor'),
        html.Div([
            dcc.Graph(
                id='nota-acceso-titulacion',
                figure={}
            ),
            dbc.Button('Ver datos', id='btn-ver-datos-2', n_clicks=0, color='primary'),
            dbc.Modal([
                dbc.ModalHeader("Datos"),
                dbc.ModalBody(html.Div(id='table-container-2')),
                dbc.ModalFooter(
                    dbc.Button("Descargar CSV", id='btn-descargar-csv-2', color='primary')
                )
            ], id='modal-2', is_open=False, size="lg")
        ], className='graph-item-resultados-gestor'),
    ], className='graphs-container-resultados-gestor')
