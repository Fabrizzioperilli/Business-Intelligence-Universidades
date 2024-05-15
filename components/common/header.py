
from dash import html, dcc, callback, Output, Input

def Header(store_id):
    return html.Div([
        html.Img(src='assets/images/logoULL.png', className='logo'),
        html.H1('Visualización de datos académicos', className='title'),
        dcc.Dropdown(
            options=[
                {'label': 'Alumno', 'value': 'Alumno'},
                {'label': 'Docente', 'value': 'Docente'},
                {'label': 'Gestor', 'value': 'Gestor'}
            ],
            value='Alumno', 
            id='dropdown_role',
            className='dropdown_role',
            clearable=False,
            searchable=False
        ),
        dcc.Store(id=store_id, storage_type='session')  # Asegura que este ID sea el correcto
    ], className='header')

@callback(
    Output('store-role', 'data'),  # Asegura que este ID sea el correcto
    Input('dropdown_role', 'value')
)
def update_role(selected_role):
    return selected_role
