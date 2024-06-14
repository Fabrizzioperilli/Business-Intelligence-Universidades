from dash import html, dcc

def create_graph(graph_id, item_class, config):
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
    ], className=item_class)
