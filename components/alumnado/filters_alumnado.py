from dash import html, dcc

def filters_alumnado():
    return html.Div([
        html.H2("Filtros"),
        html.Label("Curso Académico"),
        dcc.Dropdown(
            id='curso-academico',
            options=[
                {'label': '2018-2019', 'value': '2018-2019'},
                {'label': '2019-2020', 'value': '2019-2020'},
                {'label': '2020-2021', 'value': '2020-2021'},
            ],
            value='2019-2020'
        )
    ], className='filters')