from dash import html, dcc
from callbacks.gestor.graphs.riesgo_abandono.callback_graph_tasa_abandono_gestor import update_graph_gestor

def graphs_riesgo_abandono_gestor():
  return html.Div([
    html.Div([
      dcc.Graph(
          id='tasa-abandono-gestor',
          figure={},
      ),
    ], className='graph-item-riesgo-abandono-gestor'),
    html.Div([
      dcc.Graph(
          id='',
          figure={}
    )], className='graph-item-riesgo-abandono-gestor'),
    html.Div([
      dcc.Graph(
          id='',
          figure={}
    )], className='graph-item-riesgo-abandono-gestor'),
  ], className='graphs-container-riesgo-abandono-gestor')