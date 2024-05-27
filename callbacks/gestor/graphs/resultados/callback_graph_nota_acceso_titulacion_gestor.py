from dash import Input, Output,callback
import plotly.graph_objs as go
from data.queries import nota_media_acceso_titulacion, universidades_gestor

@callback(
    Output('nota-acceso-titulacion','figure'),
    Input('selected-gestor-store', 'data')
)
def update_grpht_gestor(gestor_id):
    fig = go.Figure()
    
    fig.update_layout(
        title={'text': 'Evolución de nota de acceso por cada titulación', 'x': 0.5},
        xaxis_title='Curso académico',
        yaxis_title='Nota media de acceso',
        showlegend=True,
        legend={'title':'Titulaciones'}
    )

    if not gestor_id:
        return fig
    
    data_universidad = universidades_gestor(gestor_id)

    if not data_universidad:
      return fig 
    
    data = nota_media_acceso_titulacion(data_universidad[0][0])
    
    if not data:
      return fig
    
    titulation_data = {}
    for row in data:
        year, titulation, score = row
        if titulation not in titulation_data:
            titulation_data[titulation] = {'years': [], 'scores': []}
        titulation_data[titulation]['years'].append(year)
        titulation_data[titulation]['scores'].append(score)
    
    # Añadir trazos al gráfico para cada titulación
    for titulation, values in titulation_data.items():
        fig.add_trace(go.Scatter(
            x=values['years'],
            y=values['scores'],
            mode='lines+markers',
            name=titulation
        ))

    return fig

    return fig


