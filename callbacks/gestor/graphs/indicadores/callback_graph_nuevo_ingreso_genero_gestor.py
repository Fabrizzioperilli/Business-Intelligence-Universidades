from dash import Input, Output, callback
import plotly.graph_objs as go
from utils.utils import list_to_tuple
from data.queries import alumnos_nuevo_ingreso_genero_titulacion, universidades_gestor



@callback(
    Output('nuevo-ingreso-genero-gestor', 'figure'),
    Input('selected-gestor-store', 'data'),
    Input('curso-academico-gestor', 'value'),
    Input('titulaciones-gestor', 'value')
)
def update_graph_gestor(docente_id, curso_academico, titulaciones):

    fig = go.Figure()

    fig.update_layout(
        barmode='stack',
        title={'text': 'Alumnos de nuevo ingreso por género y titulación', 'x': 0.5},
        xaxis=dict(title='Titulaciones'),
        yaxis=dict(title='Nº de alumnos de nuevo ingreso'),
        showlegend=True,
        legend=dict(title='Género')
    )

    if not docente_id or not curso_academico or not titulaciones:
        return fig
    
    try:
        titulaciones = list_to_tuple(titulaciones)
    except Exception as e:
        return [], None
    
    data_universidad = universidades_gestor(docente_id)
    if not data_universidad:
        return fig
    
    data = alumnos_nuevo_ingreso_genero_titulacion(curso_academico, titulaciones, data_universidad[0][0])

    if not data:
        return fig
    
        # Parsear los datos
    titulaciones = []
    hombres = []
    mujeres = []

    for row in data:
        if row[1] not in titulaciones:
            titulaciones.append(row[1])
        if row[2] == 'Masculino':
            hombres.append(row[3])
        else:
            mujeres.append(row[3])



    fig.add_trace(go.Bar(
        x=titulaciones,
        y=hombres,
        name='Hombres',
        marker_color='blue',
        opacity=0.8
    ))

    fig.add_trace(go.Bar(
        x=titulaciones,
        y=mujeres,
        name='Mujeres',
        marker_color='red',
        opacity=0.8
    ))

    return fig


