#
# @file modal_data.py
# @brief Este archivo contiene el componente para mostrar los datos de una tabla en un modal.
# @version 1.0
# @date 29/05/2024
# @license MIT License
# @author Fabrizzio Daniell Perilli Martín
# @email alu0101138589@ull.edu.es
#

from dash import html
import dash_bootstrap_components as dbc


def create_modal(modal_id, table_container_id, download_button_id, view_data_button_id):
    """
    Crea el modal para mostrar los datos de una tabla. El modal tiene un botón para descargar los datos en formato CSV.
    
    Args:
        modal_id (str): ID del modal
        table_container_id (str): ID del contenedor de la tabla
        download_button_id (str): ID del botón para descargar los datos
        view_data_button_id (str): ID del botón para abrir el modal

    Returns:
        dbc.Modal: Modal para mostrar los datos
    """
    return html.Div([
        dbc.Button('Ver datos', id=view_data_button_id, n_clicks=0, color='primary'),
        dbc.Modal([
            dbc.ModalHeader("Datos"),
            dbc.ModalBody(html.Div(id=table_container_id), style={'maxHeight': 'calc(100vh - 200px)', 'overflowY': 'auto'}),
            dbc.ModalFooter(
                dbc.Button("Descargar CSV", id=download_button_id, color='primary')
            )
        ], id=modal_id, is_open=False, size="lg")
    ])
