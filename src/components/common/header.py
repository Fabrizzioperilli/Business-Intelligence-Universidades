
from dash import html, dcc, callback, Output, Input, State

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
            id='dropdown_role',
            className='dropdown_role',
            clearable=False,
            searchable=False
        ),
        dcc.Store(id=store_id, storage_type='session')  # Utilizado para almacenar el rol entre recargas de página
    ], className='header')

@callback(
    Output('dropdown_role', 'value'),  # Actualiza el valor del dropdown basado en el almacenamiento
    Input('store-role', 'modified_timestamp'),  # Utiliza el timestamp modificado para evitar dependencias directas
    State('store-role', 'data'),  # Utiliza el estado del almacenamiento
    prevent_initial_call=True
)
def initialize_dropdown(ts, stored_role):
    return stored_role if ts is not None else 'Alumno'  # Usa el timestamp para verificar si se ha modificado

@callback(
    Output('store-role', 'data'),  # Guarda el valor seleccionado en el almacenamiento
    Input('dropdown_role', 'value'),  # Escucha los cambios en el dropdown
    State('store-role', 'data'),  # Estado actual para comparación
    prevent_initial_call=True
)
def update_role(new_role, current_role):
    if new_role != current_role:  # Verifica si el nuevo valor es diferente para evitar ciclos
        return new_role
    return current_role