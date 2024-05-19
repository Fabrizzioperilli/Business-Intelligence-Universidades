from dash import callback, Input, Output
import plotly.graph_objs as go
from data.queries import asignaturas_superadas_media_abandono
from utils.utils import list_to_tuple

@callback(
    Output('asignaturas-superadas-general-mi-nota', 'figure'),
    Input('curso-academico', 'value'),
    Input('selected-alumnado-store', 'data'),
    Input('asignaturas-matriculadas', 'value'),
    Input('titulacion-alumnado', 'value')
)
def update_graph_alumnado(curso_academico, alumno_id, asignaturas_matriculadas, titulacion):
    if not curso_academico or not alumno_id or not asignaturas_matriculadas or not titulacion: 
        return go.Figure()

    try:
        curso_academico = list_to_tuple(curso_academico)
        asignaturas_matriculadas = list_to_tuple(asignaturas_matriculadas)
    except Exception as e:
        return [], None

    data = asignaturas_superadas_media_abandono(curso_academico, asignaturas_matriculadas, titulacion)

    if not data:
        return go.Figure()

    traces = {
        'Abandono (Yo)': {'x': [], 'y': [], 'name': 'Abandono (Yo)', 'color': 'yellow'},
        'No Abandono (Yo)': {'x': [], 'y': [], 'name': 'No Abandono (Yo)', 'color': 'yellow'},
        'Abandono': {'x': [], 'y': [], 'name': 'Abandono', 'color': 'red'},
        'No Abandono': {'x': [], 'y': [], 'name': 'No Abandono', 'color': 'blue'}
    }

    for student in data:
        abandona_key = 'Abandono' if student[1].strip().lower() == 'si' else 'No Abandono'
        personal_key = ' (Yo)' if student[0] == alumno_id else ''
        key = abandona_key + personal_key 

        traces[key]['x'].append(student[2])
        traces[key]['y'].append(student[3])

    fig = go.Figure()

    # Primero, agregamos los puntos generales
    for status, trace_data in traces.items():
        if ' (Yo)' not in status:
            fig.add_trace(
                go.Scatter(
                    x=trace_data['x'], 
                    y=trace_data['y'], 
                    mode='markers', 
                    name=trace_data['name'],
                    marker=dict(
                        size=12,
                        line=dict(width=1),
                        color=trace_data['color']
                    ),
                    opacity=0.8
                )
            )

    # Luego, agregamos los puntos del usuario para que se superpongan a los anteriores
    for status, trace_data in traces.items():
        if ' (Yo)' in status:
            fig.add_trace(
                go.Scatter(
                    x=trace_data['x'], 
                    y=trace_data['y'], 
                    mode='markers', 
                    name=trace_data['name'],
                    marker=dict(
                        size=12,
                        line=dict(width=2),
                        color=trace_data['color'],
                        symbol='square'  # Cambiar el símbolo del marcador para destacar
                    ),
                    opacity=1.0
                )
            )

    fig.update_layout(
        title={'text':'Relación nota media y número de asignaturas superadas por curso académico', 'x':0.5},
        xaxis_title='Nota Media',
        yaxis_title='Número de asignaturas superadas',
        legend_title='Estado del alumno',
        showlegend=True,
        xaxis=dict(range=[0, 10]),
        yaxis=dict(range=[0, 40])
    )

    return fig
