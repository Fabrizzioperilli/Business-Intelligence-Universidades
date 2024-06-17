from dash import html, dcc
from callbacks.gestor.utils.callback_tabs_gestor import render_content


def tabs_gestor():
    """
    Crea las pestañas de la sección "Gestor". Cada pestaña contiene un conjunto de gráficos
    y tablas con los datos de los alumnos del perfil "Gestor".

    Returns:
    html.Div: Pestañas de la sección "Gestor"
    """
    
    return html.Div(
        [
            dcc.Tabs(
                id="tabs-gestor",
                value="indicadores-academicos-tab",
                children=[
                    dcc.Tab(
                        label="Indicadores académicos",
                        value="indicadores-academicos-tab",
                    ),
                    dcc.Tab(
                        label="Resultados académicos", value="resultados-academicos-tab"
                    ),
                    dcc.Tab(label="Riesgo de abandono", value="riesgo-abandono-tab"),
                    dcc.Tab(label="Recomendaciones", value="recomendaciones-tab"),
                ],
                className="tabs",
            ),
            html.Div(id="tabs-gestor-content"),
            dcc.Store(id="selected-gestor-store", storage_type="local"),
            dcc.Location(id="url", refresh=False),
        ]
    )
