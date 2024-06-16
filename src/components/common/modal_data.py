from dash import html
import dash_bootstrap_components as dbc


def create_modal(modal_id, table_container_id, download_button_id, view_data_button_id):
    """
    Crea el modal para mostrar los datos de una tabla. El modal tiene un botón para descargar los datos en formato CSV.
    
    :param modal_id: str: Id del modal.
    :param table_container_id: str: Id del contenedor de la tabla.
    :param download_button_id: str: Id del botón de descarga.
    :param view_data_button_id: str: Id del botón para ver los datos.
    :return: html.Div: Modal.
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
