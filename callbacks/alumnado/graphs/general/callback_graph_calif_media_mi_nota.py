from dash import callback, Input, Output
from data.queries import nota_media_general_mi_nota, universidad_alumno
import plotly.graph_objs as go
from utils.utils import list_to_tuple
import pandas as pd

@callback(
    Output('nota-media-general-mi-nota', 'figure'),
    Input('curso-academico', 'value'),
    Input('asignaturas-matriculadas', 'value'),
    Input('selected-alumnado-store', 'data'),
    Input('titulacion-alumnado', 'value')
)
def update_graph_alumnado(curso_academico, asignaturas_matriculadas, alumno_id, titulacion):

    fig = go.Figure()

    fig.update_layout(
            title={'text':'Nota media general y mi nota por asignaturas', 'x':0.5},
            xaxis={'title': 'Asignatura', 'tickangle': 45},
            yaxis={'title': 'Nota'},
            barmode='group',
            legend={'orientation': 'v'},
            height=600,
        )

    if not curso_academico or not asignaturas_matriculadas or not alumno_id or not titulacion:
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

    data = nota_media_general_mi_nota(curso_academico, asignaturas_matriculadas, alumno_id, titulacion, data_universidad[0][0])

    if not data:
        return fig

     # Convertir la lista de datos en un DataFrame
    df = pd.DataFrame(data, columns=['Asignatura', 'NotaMediaGeneral', 'MiNota'])

    fig.add_trace(go.Bar(
        x=df['Asignatura'],
        y=df['MiNota'],
        name='Mi nota',
        marker_color='blue',
        opacity=0.7,
    ))

    fig.add_trace(go.Bar(
        x=df['Asignatura'],
        y=df['NotaMediaGeneral'],
        name='Nota media general',
        marker_color='grey',
        opacity=0.7
    ))

    return fig