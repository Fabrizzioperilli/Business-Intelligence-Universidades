from dash import html, dcc
from callbacks.common.callback_user_role import initialize_dropdown, update_role

def Header(store_role):
    return html.Div([
        html.Img(src='assets/images/logoULL.png', className='logo'),
        html.H1('Visualización de datos académicos', className='title'),
        dcc.Dropdown(
            options=[
                {'label': 'Alumno', 'value': 'Alumno'},
                {'label': 'Docente', 'value': 'Docente'},
                {'label': 'Gestor', 'value': 'Gestor'}
            ],
            id='dropdown_role',
            className='dropdown_role',
            clearable=False,
            searchable=False,
            placeholder='Selecciona un rol',
            value='Alumno'
        ),
        dcc.Store(id=store_role, storage_type='session')
    ], className='header')