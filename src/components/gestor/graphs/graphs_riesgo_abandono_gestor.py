from dash import html, dcc
from callbacks.gestor.graphs.riesgo_abandono.callback_graph_tasa_abandono_gestor import update_graph_gestor
from callbacks.gestor.graphs.riesgo_abandono.callback_graph_tasa_graduacion_gestor import update_graph_gestor
from components.common.create_graph_with_table import create_graph_with_table
from utils.utils import config_mode_bar_buttons_gestor

def graphs_riesgo_abandono_gestor():
    graphs_info = [
        {
            'graph_id': 'tasa-abandono-gestor',
            'modal_id': 'modal-tasa-abandono',
            'table_container_id': 'table-container-tasa-abandono',
            'download_button_id': 'btn-descargar-tasa-abandono',
            'view_data_button_id': 'btn-ver-datos-tasa-abandono'
        },
        {
            'graph_id': 'tasa-graduacion-gestor',
            'modal_id': 'modal-tasa-graduacion',
            'table_container_id': 'table-container-tasa-graduacion',
            'download_button_id': 'btn-descargar-tasa-graduacion',
            'view_data_button_id': 'btn-ver-datos-tasa-graduacion'
        }
    ]
    
    graph_elements = [
        create_graph_with_table(
            graph_info['graph_id'], 
            'graph-item-riesgo-abandono-gestor', 
            config_mode_bar_buttons_gestor,
            {
                'modal_id': graph_info['modal_id'],
                'table_container_id': graph_info['table_container_id'],
                'download_button_id': graph_info['download_button_id'],
                'view_data_button_id': graph_info['view_data_button_id']
            }
        ) for graph_info in graphs_info
    ]

    return html.Div(graph_elements, className='graphs-container-riesgo-abandono-gestor')
