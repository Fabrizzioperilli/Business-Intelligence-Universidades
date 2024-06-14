from dash import Output, Input, callback
from layouts.alumno_layout import alumno_layout
from layouts.docente_layout import docente_layout
from layouts.gestor_layout import gestor_layout

@callback(
    Output('page-content', 'children'),
    Input('store-role', 'data')
)
def update_layout(role):
    if role == 'Alumno':
        return alumno_layout()
    elif role == 'Docente':
        return docente_layout()
    elif role == 'Gestor':
        return gestor_layout()
    return ""