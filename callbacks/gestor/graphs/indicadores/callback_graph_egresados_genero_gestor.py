from dash import Input, Output, callback
import plotly.graph_objects as go
from utils.utils import list_to_tuple
from data.queries import alumnos_egresados_genero_titulacion, universidades_gestor


@callback(
    Output('egresados-genero-gestor', 'figure'),
    Input('selected-gestor-store', 'data'),
    Input('curso-academico-gestor', 'value'),
    Input('titulaciones-gestor', 'value')
)
def update_graph_gestor(docente_id, curso_academico, titulaciones):
    if not docente_id or not curso_academico or not titulaciones:
        return go.Figure()
    
    try:
        titulaciones = list_to_tuple(titulaciones)
    except Exception as e:
        return go.Figure()
    
    data_universidad = universidades_gestor(docente_id)
    if not data_universidad:
        return go.Figure()
    
    data = alumnos_egresados_genero_titulacion(data_universidad[0][0], curso_academico, titulaciones)

    if not data:
        return go.Figure()
    
    # Parsear los datos
    tit_dict = {}
    for row in data:
        titulacion = row[0]
        genero = row[1]
        cantidad = row[2]
        
        if titulacion not in tit_dict:
            tit_dict[titulacion] = {'Masculino': 0, 'Femenino': 0}
        
        tit_dict[titulacion][genero] += cantidad

    titulaciones = list(tit_dict.keys())
    hombres = [tit_dict[tit]['Masculino'] for tit in titulaciones]
    mujeres = [tit_dict[tit]['Femenino'] for tit in titulaciones]

    fig = go.Figure()

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

    fig.update_layout(
        barmode='stack',
        title={'text': 'Alumnos egresados por curso académico, titulación y género', 'x': 0.5},
        xaxis=dict(title='Titulaciones'),
        yaxis=dict(title='Nº de alumnos egresados'),
        showlegend=True,
        legend=dict(title='Género')
    )

    return fig
