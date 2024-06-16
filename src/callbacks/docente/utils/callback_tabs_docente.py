from dash import html, callback, Input, Output,State
from components.docente.utils.select_docente import select_docente
from components.common.sidebar import sidebar
from components.docente.utils.resumen_docente import resumen_docente
from components.docente.filters.filter_curso_academico_docente import filter_curso_academico_docente
from components.docente.filters.filter_asignaturas_docente import filter_asignaturas_docente
from components.docente.filters.filter_titulacion_docente import filter_titulacion_docente
from components.docente.filters.filter_all_curso_academico import filter_all_curso_academico
from components.docente.filters.filter_all_asignaturas_titulacion_docente import filter_all_asignaturas_titulacion_docente
from components.docente.graphs.graphs_personal_docente import graphs_personal_docente
from components.docente.graphs.graphs_general_docente import graphs_general_docente
from components.common.filters import filters
from components.docente.utils.recomendador_docente import recomendador_docente


@callback(
    Output('tabs-docente-content', 'children'),
    Input('tabs-docente', 'value'),
    State('selected-docente-store', 'data')
    )
def render_content(tab, selected_docente):
    if tab == 'rendimiento-academico-asignatura-tab':
        return html.Div([
            select_docente(),
            html.H2("Dashboard Docente", style={'textAlign': 'center'}),
            html.Div([
                sidebar([
                  resumen_docente(),
                  filters([
                    filter_titulacion_docente(),
                    filter_asignaturas_docente(),
                    filter_curso_academico_docente()
                  ]),
                ]),
                graphs_personal_docente()
            ], className='content-layout-dashboard')
        ])
    elif tab == 'rendimiento-academico-tab':
        return html.Div([
            html.H2("Dashboard Docente", style={'textAlign': 'center'}),
            html.Div([
                sidebar([
                  resumen_docente(),
                  filters([
                    filter_titulacion_docente(),
                    filter_all_curso_academico(),
                    filter_all_asignaturas_titulacion_docente()
                  ]),
                ]),
                graphs_general_docente()
            ], className='content-layout-dashboard')
        ])
    elif tab == 'recomendaciones-tab':
        return html.Div([
            recomendador_docente()
        ])