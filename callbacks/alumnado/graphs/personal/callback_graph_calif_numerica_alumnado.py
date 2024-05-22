from dash import Input, Output, callback
import plotly.graph_objs as go
from data.queries import calif_numerica_asignatura
from utils.utils import list_to_tuple, random_color

@callback(
    Output('graph-bar-calificaciones-por-asignatura', 'figure'),
    Input('selected-alumnado-store', 'data'), 
    Input('curso-academico', 'value'),
    Input('titulacion-alumnado','value')
)
def update_graph_alumnado(alumno_id, curso_academico, titulacion):

    fig = go.Figure()

    fig.update_layout(
        title={'text': 'Calificación cuantitativa de las asignaturas matriculadas del alumno', 'x': 0.5},
        xaxis={'title': 'Asignatura', 'tickangle': 45},
        yaxis={'title': 'Calificación'},
        height=600,
        showlegend=True,
        legend=dict(
            x=1,
            y=1,
            traceorder='normal',
            font=dict(
                size=10,  # Ajusta el tamaño de la fuente para que sea más pequeño
            ),
            title='Asignaturas'
        )
    )

    if not alumno_id or not curso_academico or not titulacion:
        return fig

    try:
        curso_academico = list_to_tuple(curso_academico)
    except Exception as e:
        print("Error:", e)
        return fig
    
    data = calif_numerica_asignatura(alumno_id, curso_academico, titulacion)

    if not data:
        return fig

    subjects = []
    grades = []
    for row in data:
        subject, grade = row
        subjects.append(subject)
        grades.append(grade)

    colors = random_color(len(subjects))
    
    for subject, grade, color in zip(subjects, grades, colors):
        fig.add_trace(go.Bar(x=[subject], y=[grade], name=subject, marker_color=color, opacity=0.8))

    return fig
