from dash import html, dcc
from callbacks.alumnado.callback_graphs_alumnado import update_graphs_alumnado

def graphs_alumnado():
  return html.Div([
    html.Div([
      dcc.Graph(
          id='example-graph',
          figure={
            'data': [],
            'layout': {
              'title': 'Evolución del progreso académico del alumno',
            }
          }
    )], className='graph-item'),
    html.Div([
      dcc.Graph(
          id='graph-bar-evolucion-asignaturas-matriculadas',
          figure={}
    )], className='graph-item'),
    html.Div([
      dcc.Graph(
          id='example-graph-3',
          figure={
            'data': [],
            'layout': {
              'title': 'Calificaciones por asignatura y curso académico',
            }
          }
    )], className='graph-item'),
    html.Div([
      dcc.Graph(
          id='example-graph-4',
          figure={
            'data': [],
            'layout': {
              'title': 'Tasa de éxito por curso académico',
            }
          }
    )], className='graph-item')
  ], className='graphs-container')            
  
