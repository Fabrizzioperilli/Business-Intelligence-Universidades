from dash import html, dcc
from callbacks.alumnado.utils.callback_select_alumnado import store_selected_alumnado


def select_alumnado():
    """
    Crea el desplegable para seleccionar un alumno.
    """
    return html.Div(
        [
            html.Div(
                [
                    dcc.Dropdown(
                        options=[],
                        value=None,
                        id="alumnado-dropdown",
                        clearable=False,
                        placeholder="Seleccione un alumno",
                    )
                ],
                className="select-alumnado",
            ),
        ]
    )
