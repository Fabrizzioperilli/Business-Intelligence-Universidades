from dash import Input, Output, State, html, callback
from components.common.sidebar import sidebar
from components.gestor.utils.select_gestor import select_gestor
from components.gestor.utils.resumen_gestor import resumen_gestor
from components.common.filters import filters
from components.gestor.filters.filter_curso_academico_gestor import filter_curso_academico_gestor
from components.gestor.filters.filter_titulaciones_gestor import filter_titulaciones_gestor
from components.gestor.filters.filter_all_curso_academico_gestor import filter_all_curso_academico_gestor
from components.gestor.graphs.graphs_indicadores_gestor import graphs_indicadores_gestor
from components.gestor.graphs.graphs_resultados_gestor import graphs_resultados_gestor
from components.gestor.graphs.graphs_riesgo_abandono_gestor import graphs_riesgo_abandono_gestor
from components.gestor.utils.recomendador_gestor import recomendador_gestor

@callback(
        Output('tabs-gestor-content', 'children'),
        Input('tabs-gestor', 'value'),
        State('selected-gestor-store', 'data')
        )
def render_content(tab, selected_gestor):
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



