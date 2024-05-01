from dash import html, dcc

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
          id='example-graph-2',
          figure={
            'data': [],
            'layout': {
              'title': 'Evolución de asignaturas matriculadas<br>por curso académico',
            }
          }
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
  
