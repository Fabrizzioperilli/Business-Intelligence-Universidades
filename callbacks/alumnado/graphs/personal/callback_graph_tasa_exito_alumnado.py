from dash import Input, Output, callback
import plotly.graph_objs as go
from data.queries import asignaturas_matriculadas_y_superadas
from utils.utils import list_to_tuple

@callback(
    Output('graph-bar-tasa-exito', 'figure'),
    Input('selected-alumnado-store', 'data'), 
    Input('curso-academico', 'value'),
    Input('titulacion-alumnado','value')

)
def update_graph_alumnado(alumno_id, curso_academico, titulacion):

    fig = go.Figure()
    
    fig.update_layout(
        title={'text': 'Tasa de éxito por curso académico del alumno', 'x': 0.5},
        xaxis={'title': 'Porcentaje de éxito'},
        yaxis={'title': 'Curso académico'},
        showlegend=False,
    )

    if not alumno_id or not curso_academico or not titulacion:
        return fig
    
    try:
        curso_academico = list_to_tuple(curso_academico)
    except Exception as e:
        print("Error:", e)
        return fig

    data = asignaturas_matriculadas_y_superadas(alumno_id, curso_academico, titulacion)
   
    if not data:
        return fig

    academic_years = [row[0] for row in data]
    success_rates = [(row[2] / row[1]) * 100 for row in data]

    fig.add_trace(go.Bar(
        x=success_rates,
        y=academic_years,
        orientation='h',
        marker_color='blue',
        opacity=0.7,
        width=0.7
    ))

    return fig
