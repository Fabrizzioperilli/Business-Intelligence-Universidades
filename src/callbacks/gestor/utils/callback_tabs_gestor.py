#
# @file callback_tabs_gestor.py
# @brief Este fichero contiene el callback para renderizar el 
#        contenido de las pestañas de la sección "Gestor".
# @version 1.0
# @date 17/05/2024
# @license MIT License
# @author Fabrizzio Daniell Perilli Martín
# @email alu0101138589@ull.edu.es
#

from dash import Input, Output, State, html, callback
from components.common.sidebar import sidebar
from components.common.filters import filters
from components.gestor.utils.select_gestor import select_gestor
from components.gestor.utils.resumen_gestor import resumen_gestor
from components.gestor.utils.recomendador_gestor import recomendador_gestor
from components.gestor.filters.filter_curso_academico_gestor import filter_curso_academico_gestor
from components.gestor.filters.filter_titulaciones_gestor import filter_titulaciones_gestor
from components.gestor.filters.filter_all_curso_academico_gestor import filter_all_curso_academico_gestor
from components.gestor.graphs.graphs_indicadores_gestor import graphs_indicadores_gestor
from components.gestor.graphs.graphs_resultados_gestor import graphs_resultados_gestor
from components.gestor.graphs.graphs_riesgo_abandono_gestor import graphs_riesgo_abandono_gestor

@callback(
    Output('tabs-gestor-content', 'children'),
    Input('tabs-gestor', 'value'),
    State('selected-gestor-store', 'data')
)
def render_content(tab, selected_gestor):
    """
    Renderiza el contenido de las pestañas de la sección "Gestor".
    
    Args:
        tab (str): Pestaña seleccionada
        selected_gestor (dict): Datos del gestor seleccionado
        
    Returns:
        html.Div: Contenido de la pestaña seleccionada
    """
    
    if tab == 'indicadores-academicos-tab':
        return html.Div([
            select_gestor(),
            html.H2("Dashboard Gestor", style={'textAlign': 'center'}),
            html.Div([
                sidebar([
                    resumen_gestor(),
                    filters([
                        filter_curso_academico_gestor(),
                        filter_titulaciones_gestor()
                    ]),
                ]),
                graphs_indicadores_gestor()
            ], className='content-layout-dashboard')

        ])
    elif tab == 'resultados-academicos-tab':
        return html.Div([
            html.H2("Dashboard Gestor", style={'textAlign': 'center'}),
             html.Div([
                sidebar([
                    resumen_gestor(),
                ]),
                graphs_resultados_gestor()
            ], className='content-layout-dashboard')
        ])
    elif tab == 'riesgo-abandono-tab':
        return html.Div([
           html.H2("Dashboard Gestor", style={'textAlign': 'center'}),
             html.Div([
                sidebar([
                    resumen_gestor(),
                    filters([
                        filter_all_curso_academico_gestor()
                    ]),
                ]),
                graphs_riesgo_abandono_gestor()
            ], className='content-layout-dashboard')
        ])
    elif tab == 'recomendaciones-tab':
        return html.Div([
            recomendador_gestor()
        ])



