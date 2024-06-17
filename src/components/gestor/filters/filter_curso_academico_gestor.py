from dash import html, dcc
from callbacks.gestor.filters.callback_filter_curso_academico_gestor import update_filter_curso_academico_gestor


def filter_curso_academico_gestor():
    """
    Crea el filtro de curso académico para el perfil "Gestor" de la pestaña
    "Indicadores académicos".

    Returns:
    html.Div: Componente con el filtro de curso académico
    """
    return html.Div(
        [
            html.Label("Curso académico"),
            dcc.Dropdown(
                id="curso-academico-gestor",
                searchable=True,
                multi=False,
                clearable=False,
                options=[],
                value=None,
                maxHeight=300,
                placeholder="Selecciona una opción",
            ),
        ]
    )
