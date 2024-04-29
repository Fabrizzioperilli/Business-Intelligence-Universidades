from dash import html, dcc

def graphs_alumnado():
  return html.Div([
    html.Div([
      dcc.Graph(
          id='example-graph',
          figure={}
    )], className='graph-item'),
    html.Div([
      dcc.Graph(
          id='example-graph-2',
          figure={}
    )], className='graph-item'),
    html.Div([
      dcc.Graph(
          id='example-graph-3',
          figure={}
    )], className='graph-item'),
    html.Div([
      dcc.Graph(
          id='example-graph-4',
          figure={}
    )], className='graph-item'),
  ], className='graphs-container')            
  
                
                  
