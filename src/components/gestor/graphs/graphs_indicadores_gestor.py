from dash import html
from callbacks.gestor.graphs.indicadores.callback_graph_nuevo_ingreso_genero_gestor import update_graph_gestor
from callbacks.gestor.graphs.indicadores.callback_graph_egresados_genero_gestor import update_graph_gestor
from callbacks.gestor.graphs.indicadores.callback_graph_nuevo_ingreso_nacionalidad_gestor import update_graph_gestor
from callbacks.gestor.graphs.indicadores.callback_graph_egresados_nacionalidad_gestor import update_graph_gestor
from components.common.create_graph_with_table import create_graph_with_table
from util import config_mode_bar_buttons_gestor

def graphs_indicadores_gestor():
    graphs_info = [
        {
            'graph_id': 'nuevo-ingreso-genero-gestor',
            'modal_id': 'modal-nuevo-ingreso-genero',
            'table_container_id': 'table-container-nuevo-ingreso-genero',
            'download_button_id': 'btn-descargar-nuevo-ingreso-genero',
            'view_data_button_id': 'btn-ver-datos-nuevo-ingreso-genero'
        },
        {
            'graph_id': 'nuevo_ingreso_nacionalidad-gestor',
            'modal_id': 'modal-nuevo-ingreso-nacionalidad',
            'table_container_id': 'table-container-nuevo-ingreso-nacionalidad',
            'download_button_id': 'btn-descargar-nuevo-ingreso-nacionalidad',
            'view_data_button_id': 'btn-ver-datos-nuevo-ingreso-nacionalidad'
        },
        {
            'graph_id': 'egresados-genero-gestor',
            'modal_id': 'modal-egresados-genero',
            'table_container_id': 'table-container-egresados-genero',
            'download_button_id': 'btn-descargar-egresados-genero',
            'view_data_button_id': 'btn-ver-datos-egresados-genero'
        },
        {
            'graph_id': 'egresados-nacionalidad-gestor',
            'modal_id': 'modal-egresados-nacionalidad',
            'table_container_id': 'table-container-egresados-nacionalidad',
            'download_button_id': 'btn-descargar-egresados-nacionalidad',
            'view_data_button_id': 'btn-ver-datos-egresados-nacionalidad'
        }
    ]
    
    graph_elements = [
        create_graph_with_table(
            graph_info['graph_id'], 
            'graph-item-indicadores-gestor', 
            config_mode_bar_buttons_gestor,
            {
                'modal_id': graph_info['modal_id'],
                'table_container_id': graph_info['table_container_id'],
                'download_button_id': graph_info['download_button_id'],
                'view_data_button_id': graph_info['view_data_button_id']
            }
        ) for graph_info in graphs_info
    ]

    return html.Div(graph_elements, className='graphs-container-indicadores-gestor')
