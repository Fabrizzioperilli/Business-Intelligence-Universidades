from dash import html, callback, Input, Output,State
from components.docente.select_docente import select_docente
from components.common.sidebar import sidebar
from components.docente.resumen_docente import resumen_docente
from components.docente.filter_curso_academico_docente import filter_curso_academico_docente
from components.docente.filter_asignaturas_docente import filter_asignaturas_docente
from components.docente.graphs_personal_docente import graphs_personal_docente

@callback(
    Output('tabs-docente-content', 'children'),
    [Input('tabs-docente', 'value')],
    State('selected-docente-store', 'data'))
def render_content(tab, selected_docente):
    if tab == 'rendimiento-academico-asignatura-tab':
        return html.Div([
            select_docente(),
            html.H2("Dashboard Docente", style={'textAlign': 'center'}),
            html.Div([
                sidebar([
                  resumen_docente(),
                  filter_curso_academico_docente(),
                  filter_asignaturas_docente()
                ]),
                graphs_personal_docente()
            ], className='content-layout-dashboard')
        ])
    elif tab == 'rendimiento-academico-tab':
        return html.Div([
            html.H3("Rendimiento Académico")
        ])
    else:
        return html.Div([
            html.H3("Rendimiento académico por asignatura")
        ])