from dash import html, dcc
from callbacks.alumnado.graphs.general.callback_graph_calif_cual_comparativa import update_graph_alumnado
from callbacks.alumnado.graphs.general.callback_graph_calif_media_mi_nota import update_graph_alumnado

def graphs_general_alumnado():
  return html.Div([
    html.Div([
      dcc.Graph(
          id='',
          figure={}
    )], className='graph-item'),
    html.Div([
      dcc.Graph(
          id='nota-cualitativa-general-mi-nota',
          figure={}
    )], className='graph-item'),
    html.Div([
      dcc.Graph(
          id='nota-media-general-mi-nota',
          figure={},
    )], className='graph-item'),
  ], className='graphs-container')            
  
