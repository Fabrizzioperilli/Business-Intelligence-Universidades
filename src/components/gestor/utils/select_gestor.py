from dash import html, dcc
from callbacks.gestor.utils.callback_select_gestor import store_selected_gestor


def select_gestor():
    """
    Crea un dropdown para seleccionar un gestor.
    
    Returns:
    html.Div: Dropdown para seleccionar un gestor
    """
    
    return html.Div(
        [
            html.Div(
                [
                    dcc.Dropdown(
                        options=[],
                        value=None,
                        id="gestor-dropdown",
                        clearable=False,
                        placeholder="Seleccione un gestor",
                    )
                ],
                className="select-gestor",
            ),
        ]
    )
