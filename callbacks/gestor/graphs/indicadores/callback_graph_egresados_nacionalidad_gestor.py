from dash import Input, Output, callback
import plotly.graph_objs as go
from utils.utils import list_to_tuple
from data.queries import alumnos_egresados_nacionalidad_titulacion, universidades_gestor


@callback(
    Output('egresados-nacionalidad-gestor','figure'),
    Input('selected-gestor-store', 'data'),
    Input('curso-academico-gestor', 'value'),
    Input('titulaciones-gestor', 'value')
)
def update_graph_gestor(gestor_id, curso_academico, titulaciones):

    fig = go.Figure()

    fig.update_layout(
        barmode='stack',
        title={'text': 'Alumnos egresados por curso académico y nacionalidad', 'x': 0.5},
        xaxis=dict(title='Titulaciones'),
        yaxis=dict(title='Nº de alumnos egresados'),
        showlegend=True,
        legend=dict(title='Nacionalidad')
    )

    if not gestor_id or not curso_academico or not titulaciones:
        return fig
    
    try:
        titulaciones = list_to_tuple(titulaciones)
    except Exception as e:
        return fig
    
    data_universidad = universidades_gestor(gestor_id)
    if not data_universidad:
        return fig

    data = alumnos_egresados_nacionalidad_titulacion(data_universidad[0][0], curso_academico, titulaciones)

    if not data:
        return fig

    # Parsear los datos
    tit_dict = {}
    nacionalidades = set()
    for row in data:
        titulacion = row[0]
        nacionalidad = row[1]
        cantidad = row[2]
        
        if titulacion not in tit_dict:
            tit_dict[titulacion] = {}
        
        if nacionalidad not in tit_dict[titulacion]:
            tit_dict[titulacion][nacionalidad] = 0

        tit_dict[titulacion][nacionalidad] += cantidad
        nacionalidades.add(nacionalidad)

    titulaciones = list(tit_dict.keys())
    nacionalidades = list(nacionalidades)

   

    for nacionalidad in nacionalidades:
        cantidades = [tit_dict[tit].get(nacionalidad, 0) for tit in titulaciones]
        fig.add_trace(go.Bar(
            x=titulaciones,
            y=cantidades,
            name=nacionalidad,
        ))


    return fig
