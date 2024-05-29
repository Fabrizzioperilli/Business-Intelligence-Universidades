from dash import html

def Footer():
    return html.Div([
        html.P('2023-2024 Universidad de la Laguna - Visualización de datos académicos'),
        html.P('Pabellón de Gobierno, C/ Padre Herrera s/n Apartado Postal 456 38200, San Cristóbal de La Laguna'),
        html.P('Santa Cruz de Tenerife - España')], className='footer')