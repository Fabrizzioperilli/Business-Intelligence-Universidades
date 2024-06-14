from components.common.create_graph import create_graph
from components.common.modal_data import create_modal
from dash import html, dcc


def create_graph_with_table(graph_id, item_class, config, modal_config):
    return html.Div([
        dcc.Loading(
            children=[
                dcc.Graph(
                    id=graph_id,
                    figure={},
                    config=config
                )
            ]
        ),
        create_modal(**modal_config)
    ], className=item_class)