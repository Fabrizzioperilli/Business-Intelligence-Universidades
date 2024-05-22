from dash import Input, Output, State, html, callback
from components.common.sidebar import sidebar
from components.gestor.select_gestor import select_gestor
from components.gestor.resumen_gestor import resumen_gestor
from components.common.filters import filters
from components.gestor.filter_curso_academico_gestor import filter_curso_academico_gestor
from components.gestor.filter_titulaciones_gestor import filter_titulaciones_gestor
from components.gestor.graphs_indicadores_gestor import graphs_indicadores_gestor

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
            html.H3("Resultados académicos")
        ])
    elif tab == 'riesgo-abandono-tab':
        return html.Div([
            html.H2("Dashboard Gestor", style={'textAlign': 'center'}),
            html.H3("Riesgo de abandono")
        ])
    else:
        return html.Div([
            html.H3("Indicadores académicos")
        ])


