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
    if not alumno_id or not curso_academico or not titulacion:
        return go.Figure()
    
    try:
        curso_academico = list_to_tuple(curso_academico)
    except Exception as e:
        return [], None

    data = asignaturas_matriculadas_y_superadas(alumno_id, curso_academico, titulacion)
   
    if not data:
        print("No data returned from the query.")
        return go.Figure()

    academic_years = [row[0] for row in data]
    success_rates = [(row[2] / row[1]) * 100 for row in data]

    trace = go.Bar(
        x=success_rates,
        y=academic_years,
        orientation='h',
        marker_color='blue',
        opacity=0.7,
        width=0.7

    )
    layout = go.Layout(
        title={'text': 'Tasa de éxito por curso académico del alumno', 'x': 0.5},
        xaxis={'title': 'Porcentaje de éxito'},
        yaxis={'title': 'Curso académico'},
        showlegend=False,
    )

    figure = go.Figure(data=[trace], layout=layout)
    return figure
