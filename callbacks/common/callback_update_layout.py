from dash import Output, Input, callback
from layouts.alumno_layout import alumno_layout
from layouts.docente_layout import docente_layout
from layouts.gestor_layout import gestor_layout

@callback(
    Output('page-content', 'children'),
    [Input('store-role', 'data')]
)
def update_layout(role):
    if role == 'Alumno':
        layout = alumno_layout()
    elif role == 'Docente':
        layout = docente_layout()
    elif role == 'Gestor':
        layout = gestor_layout()
    return layout