#
# @file header.py
# @brief Este archivo contiene el componente del header de la aplicación.
# @version 1.0
# @date 25/04/2024
# @license MIT License
# @author Fabrizzio Daniell Perilli Martín
# @email alu0101138589@ull.edu.es
#

from dash import html, dcc
from callbacks.common.callback_user_role import initialize_dropdown, update_role


def header(store_role):
    """
    Contiene el header de la aplicación y el desplegable para seleccionar el rol.

    Args:
        store_role: str: ID del store que contiene el rol del usuario

    Returns:
        html.Div: Header de la aplicación
    """
    return html.Div(
        [
            html.Img(src="assets/images/logoULL.png", className="logo"),
            html.H1("Visualización de datos académicos", className="title"),
            dcc.Dropdown(
                options=[
                    {"label": "Alumno", "value": "Alumno"},
                    {"label": "Docente", "value": "Docente"},
                    {"label": "Gestor", "value": "Gestor"},
                ],
                id="dropdown_role",
                className="dropdown_role",
                clearable=False,
                searchable=False,
                placeholder="Selecciona un rol",
                value="Alumno",
            ),
            dcc.Store(id=store_role, storage_type="session"),
        ],
        className="header",
    )
