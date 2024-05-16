from dash import callback, Input, Output
import plotly.graph_objs as go
from data.db_connector import db
from utils.utils import list_to_tuple

@callback(
    Output('graph-alumnos-nota-media', 'figure'),
    [Input('asignaturas-docente', 'value')],
    [Input('curso-academico-docente', 'value')],
    [Input('selected-docente-store', 'data')]
)
def update_graph_docente(asignaturas, curso_academico, docente_id):
    if not asignaturas or not curso_academico or not docente_id:
        return go.Figure()
    
    try:
        curso_academico = list_to_tuple(curso_academico)
        asignaturas = list_to_tuple(asignaturas)
    except Exception as e:
        return go.Figure()
    
    query = """
    SELECT
        l.curso_aca,  
        l.asignatura, 
        AVG(l.calif_numerica) AS media_calif
    FROM 
        lineas_actas l
    WHERE 
        l.asignatura IN :asignaturas AND 
        l.curso_aca IN :curso_academico
    GROUP BY 
        l.curso_aca,
        l.asignatura
    ORDER BY 
        l.curso_aca,
        l.asignatura;
    """

    params = {
        'curso_academico': curso_academico,
        'asignaturas': asignaturas
    }

    try:
        data = db.execute_query(query, params)
    except Exception as e:
        print("Query execution failed:", e)
        return go.Figure()
    
    if not data:
        return go.Figure()
    
    curso_academico = [x[0] for x in data]
    asignatura = [x[1] for x in data]
    media_calif = [x[2] for x in data]

    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=curso_academico,
        y=media_calif,
        name='Nota media',
        marker=dict(color='blue'),
        opacity=0.8
    ))

    fig.update_layout(
        title={'text': 'Nota media por asignatura y curso académico', 'x': 0.5},
        xaxis_title='Curso académico',
        yaxis_title='Nota media',
        xaxis=dict(type='category')  # Ensures the x-axis uses categorical data
        
    )
    
    return fig

        



