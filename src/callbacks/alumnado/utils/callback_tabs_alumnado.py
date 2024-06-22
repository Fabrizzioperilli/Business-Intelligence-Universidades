#
# @file callback_tabs_alumnado.py
# @brief Este fichero contiene el callback para renderizar el contenido 
#        de las pestañas del dashboard del alumnado
# @version 1.0
# @date 29/04/2024
# @license MIT License
# @author Fabrizzio Daniell Perilli Martín
# @email alu0101138589@ull.edu.es
#

from dash import html, callback, Output, Input, State
from components.common.sidebar import sidebar
from components.common.filters import filters
from components.alumnado.utils.select_alumnado import select_alumnado
from components.alumnado.utils.recomendador_alumnado import recomendador_alumnado
from components.alumnado.utils.resumen_alumnado import resumen_alumnado
from components.alumnado.filters.filter_curso_academico_alumnado import filter_curso_academico_alumnado
from components.alumnado.filters.filter_asignaturas_matri_alumnado import filter_asignaturas_matri_alumnado
from components.alumnado.filters.filter_titulacion_alumnado import filter_titulacion_alumnado
from components.alumnado.graphs.graphs_general_alumnado import graphs_general_alumnado
from components.alumnado.graphs.graphs_personal_alumnado import graphs_personal_alumnado


@callback(
    Output('tabs-alumnado-content', 'children'),
    Input('tabs-alumnado', 'value'),
    State('selected-alumnado-store', 'data')
)
def render_content(tab, selected_alumnado):
    """
    Renderiza el contenido de las pestañas del dashboard del alumnado.

    Args:
        tab (str): Pestaña seleccionada
        selected_alumnado (str): Alumno seleccionado

    Returns:
        list: Componentes de la pestaña seleccionada
        
    """
    if tab == 'expediente-personal-tab':
        return html.Div([
            select_alumnado(),
            html.H2("Dashboard Alumnado", style={'textAlign': 'center'}),
            html.Div([
                sidebar([
                    resumen_alumnado(), 
                    filters([
                        filter_titulacion_alumnado(),
                        filter_curso_academico_alumnado()
                        ])
                    ]),
                graphs_personal_alumnado()
            ], className='content-layout-dashboard')
        ])
    elif tab == 'rendimiento-academico-tab':
        return html.Div([
            html.H2("Dashboard Alumnado", style={'textAlign': 'center'}),
            html.Div([
                sidebar([
                    resumen_alumnado(),
                    filters([
                        filter_titulacion_alumnado(),
                        filter_curso_academico_alumnado(),
                        filter_asignaturas_matri_alumnado()
                        ])
                    ]),
                graphs_general_alumnado()
            ], className='content-layout-dashboard')
        ])
    elif tab == 'recomendador-tab':
        return html.Div([
            recomendador_alumnado()
        ])
    