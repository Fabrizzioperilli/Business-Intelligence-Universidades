from dash import html

def filters(filters):
    return html.Div([
        html.H2("Filtros"),
        html.Div(filters)
    ], className='filters')