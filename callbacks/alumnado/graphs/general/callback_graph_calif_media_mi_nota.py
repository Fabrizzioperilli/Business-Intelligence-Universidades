from dash import callback, Input, Output
from data.queries import nota_media_general_mi_nota
import plotly.graph_objs as go
from utils.utils import list_to_tuple

@callback(
    Output('nota-media-general-mi-nota', 'figure'),
    Input('curso-academico', 'value'),
    Input('asignaturas-matriculadas', 'value'),
    Input('selected-alumnado-store', 'data'),
    Input('titulacion-alumnado', 'value')
)

def update_graph_alumnado(curso_academico, asignaturas_matriculadas, alumno_id, titulacion):
    if not curso_academico or not asignaturas_matriculadas or not alumno_id or not titulacion:
        return go.Figure()

    try:
        curso_academico = list_to_tuple(curso_academico)
        asignaturas_matriculadas = list_to_tuple(asignaturas_matriculadas)
    except Exception as e:
        return [], None


    data = nota_media_general_mi_nota(curso_academico, asignaturas_matriculadas, alumno_id, titulacion)

    if not data:
        return go.Figure()

    all_subjects = [row[0] for row in data]
    avg_grades = [row[1] for row in data]
    student_grades = [row[2] for row in data]

    traces = [
        go.Bar(
            x=all_subjects,
            y=student_grades,
            name='Mi nota',
            marker_color='blue',
            opacity=0.8,
        ),
        go.Bar(
            x=all_subjects,
            y=avg_grades,
            name='Nota media general',
            marker_color='grey',
            opacity=0.8
        )
    ]

    layout = go.Layout(
        title={'text':'Nota media general y mi nota por asignaturas y curso académico', 'x':0.5},
        xaxis={'title': 'Asignatura', 'tickangle': 45},
        yaxis={'title': 'Nota'},
        barmode='group',
        legend={'orientation': 'v'},
        height=600,
    )

    return go.Figure(data=traces, layout=layout)
        
        

