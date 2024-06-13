from dash import html, dcc

def filters(filters):
    return html.Div([
        html.H2("Filtros"),
        html.Div(filters)
    ], className='filters')