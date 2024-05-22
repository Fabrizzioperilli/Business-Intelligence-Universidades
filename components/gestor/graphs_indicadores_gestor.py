from dash import html, dcc
from callbacks.gestor.graphs.indicadores.callback_graph_nuevo_ingreso_genero_gestor import update_graph_gestor
from callbacks.gestor.graphs.indicadores.callback_graph_egresados_genero_gestor import update_graph_gestor
from callbacks.gestor.graphs.indicadores.callback_graph_nuevo_ingreso_nacionalidad_gestor import update_graph_gestor
from callbacks.gestor.graphs.indicadores.callback_graph_egresados_nacionalidad_gestor import update_graph_gestor

def graphs_indicadores_gestor():
  return html.Div([
    html.Div([
      dcc.Graph(
          id='nuevo-ingreso-genero-gestor',
          figure={},
    )], className='graph-item-personal-docente'),
    html.Div([
      dcc.Graph(
          id='egresados-genero-gestor',
          figure={}
    )], className='graph-item-personal-docente'),
    html.Div([
      dcc.Graph(
          id='nuevo_ingreso_nacionalidad-gestor',
          figure={},
    )], className='graph-item-personal-docente'),
    html.Div([
      dcc.Graph(
          id='egresados-nacionalidad-gestor',
          figure={}
    )], className='graph-item-personal-docente')
  ], className='graphs-container-indicadores-gestor')