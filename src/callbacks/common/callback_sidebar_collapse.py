#
# @file callback_sidebar_collapse.py
# @brief Este fichero contiene el callback para colapsar y descolapsar el sidebar
# @version 1.0
# @date 29/04/2024
# @license MIT License
# @author Fabrizzio Daniell Perilli Martín
# @email alu0101138589@ull.edu.es
#

from dash import Output, Input, State, callback


@callback(
    Output("collapse", "is_open"),
    Input("sidebar-toggle", "n_clicks"),
    State("collapse", "is_open"),
)
def sidebar_collapse(n, is_open):
    """
    Callback que permite colapsar y descolapsar el sidebar.

    Args:
        n (int): Número de clicks
        is_open (bool): Estado del sidebar

    Returns:
        bool: Estado del sidebar
    """
    if n:
        return not is_open
    return is_open
