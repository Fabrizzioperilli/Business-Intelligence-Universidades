from dash import callback, Input, Output
from data.queries import calif_cualitativa_comparativa, calif_cualitativa_alumno_asignaturas, universidad_alumno
import plotly.graph_objs as go
import pandas as pd
from utils.utils import list_to_tuple

@callback(
    Output('nota-cualitativa-general-mi-nota', 'figure'),
    Input('curso-academico', 'value'),
    Input('asignaturas-matriculadas', 'value'),
    Input('selected-alumnado-store', 'data'),
    Input('titulacion-alumnado', 'value')
)
def update_graph_alumnado(curso_academico, asignaturas_matriculadas, alumno_id, titulacion):

    fig = go.Figure()

    fig.update_layout(
        title={'text': 'Calificaciones cualitativas general por curso académico', 'x': 0.5},
        barmode='stack',
        xaxis={'title': 'Asignatura', 'tickangle': 45},
        yaxis={'title': 'Nº Alumnos matriculados'},
        showlegend=True,
        legend={'title': 'Calificación'},
        height=600,
    )

    if not (curso_academico and asignaturas_matriculadas and alumno_id and titulacion):
        return fig

    try:
        curso_academico = list_to_tuple(curso_academico)
        asignaturas_matriculadas = list_to_tuple(asignaturas_matriculadas)
    except Exception as e:
        print("Error:", e)
        return fig
    
    data_universidad = universidad_alumno(alumno_id)

    if not data_universidad:
        return fig

    general_data = calif_cualitativa_comparativa(curso_academico, asignaturas_matriculadas, titulacion, data_universidad[0][0])
    student_data = calif_cualitativa_alumno_asignaturas(alumno_id, curso_academico, asignaturas_matriculadas, titulacion)

    if not general_data:
        return fig

    general_df = pd.DataFrame(general_data, columns=['Asignatura', 'Calificacion', 'Numero'])
    student_df = pd.DataFrame(student_data, columns=['Asignatura', 'Calificacion', 'Numero'])

    categories = ['Suspenso', 'No presentado', 'Aprobado', 'Notable', 'Sobresaliente']
    
    color_mapping = {
        'Sobresaliente': 'blue', 
        'Notable': 'green', 
        'Aprobado': 'orange', 
        'Suspenso': 'red', 
        'No presentado': 'gray'
        }

    general_pivot = general_df.pivot_table(index='Asignatura', columns='Calificacion', values='Numero', fill_value=0)
    general_pivot = general_pivot.reindex(columns=categories, fill_value=0)

    for category in categories:
        fig.add_trace(
            go.Bar(
                x=general_pivot.index,
                y=general_pivot[category],
                name=category,
                marker=dict(color=color_mapping[category]),
                opacity=0.7
            )
        )

    for category in categories:
        y = [
            1 if (
                (subject in student_df['Asignatura'].values) and 
                (student_df[student_df['Asignatura'] == subject]['Calificacion'].values[0] == category)
            ) else 0 for subject in general_pivot.index
        ]
        fig.add_trace(
            go.Bar(
                x=general_pivot.index,
                y=y,
                name=f"{category} (Yo)",
                marker=dict(color=color_mapping[category], line=dict(color='black', width=2)),
                opacity=1
            )
        )

    return fig
