# components.py
from dash import html
import dash_bootstrap_components as dbc


def create_modal(modal_id, table_container_id, download_button_id, view_data_button_id):
    return html.Div([
        dbc.Button('Ver datos', id=view_data_button_id, n_clicks=0, color='primary'),
        dbc.Modal([
            dbc.ModalHeader("Datos"),
            dbc.ModalBody(html.Div(id=table_container_id)),
            dbc.ModalFooter(
                dbc.Button("Descargar CSV", id=download_button_id, color='primary')
            )
        ], id=modal_id, is_open=False, size="lg")
    ])
