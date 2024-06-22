#
# @file footer.py
# @brief Este archivo contiene el footer de la aplicación.
# @version 1.0
# @date 25/04/2024
# @license MIT License
# @author Fabrizzio Daniell Perilli Martín
# @email alu0101138589@ull.edu.es
#

from dash import html


def footer():
    """
    Retorna el footer de la aplicación

    Returns:
        html.Div: Footer de la aplicación
    """
    return html.Div([
        html.P('2023-2024 Universidad de la Laguna - Visualización de datos académicos'),
        html.P('Pabellón de Gobierno, C/ Padre Herrera s/n Apartado Postal 456 38200, San Cristóbal de La Laguna'),
        html.P('Santa Cruz de Tenerife - España')], className='footer')