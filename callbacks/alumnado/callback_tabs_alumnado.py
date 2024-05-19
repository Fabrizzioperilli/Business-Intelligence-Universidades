from dash import html, callback, Output, Input, State
from components.common.sidebar import sidebar
from components.alumnado.graphs_personal_alumnado import graphs_personal_alumnado
from components.alumnado.graphs_general_alumnado import graphs_general_alumnado
from components.alumnado.select_alumnado import select_alumnado
from components.alumnado.resumen_alumnado import resumen_alumnado
from components.common.filters import filters
from components.alumnado.filter_curso_academico_alumnado import filter_curso_academico_alumnado
from components.alumnado.filter_asignaturas_matri_alumnado import filter_asignaturas_matri_alumnado
from components.alumnado.filter_titulacion_alumnado import filter_titulacion_alumnado
from components.alumnado.recomendador_alumnado import recomendador_alumnado



@callback(
    Output('tabs-alumnado-content', 'children'),
    [Input('tabs-alumnado', 'value')],
    State('selected-alumnado-store', 'data')
)
def render_content(tab, selected_alumnado):
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