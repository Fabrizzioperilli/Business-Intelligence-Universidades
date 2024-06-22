#
# @file filters.py
# @brief Este archivo contiene componente que contiene los filtros de la aplicación.
# @version 1.0
# @date 28/04/2024
# @license MIT License
# @author Fabrizzio Daniell Perilli Martín
# @email alu0101138589@ull.edu.es
#

from dash import html


def filters(filters):
    """
    Crea un componente que contiene los filtros de la aplicación.
    
    Args:
        filters (list): Lista de filtros

    Returns:
        html.Div: Componente que contiene los filtros
    """
    return html.Div([html.H2("Filtros"), html.Div(filters)], className="filters")
