from dash import Input, Output, callback
import plotly.graph_objs as go
from data.queries import asignaturas_superadas
from utils.utils import list_to_tuple


@callback(
    Output('graph-evolucion-progreso-academico', 'figure'),
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

    data = asignaturas_superadas(alumno_id, curso_academico, titulacion)

    if not data:
        print("No data returned from the query.")
        return go.Figure()

    academic_years = [row[0] for row in data]
    subjects_passed = [row[1] for row in data]


    cumulative_passed = []
    cumulative_total = 0
    for count in subjects_passed:
        cumulative_total += count
        cumulative_passed.append(cumulative_total)

    trace = go.Bar(x=academic_years, y=cumulative_passed, marker_color='blue', opacity=0.7)

    layout = go.Layout(
        title={'text':'Evolución del progreso académico del alumno', 'x':0.5},
        xaxis={'title': 'Curso académico'},
        yaxis={'title': 'Nº Asignaturas de superadas (Acumulativo)'},
        showlegend=False,
    )

    figure = go.Figure(data=[trace], layout=layout)
    return figure