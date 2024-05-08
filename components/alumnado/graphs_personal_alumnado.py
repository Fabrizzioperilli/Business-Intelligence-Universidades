from dash import html, dcc
from callbacks.alumnado.graphs.personal.callback_graph_calif_cualitativa_alumnado import update_graph_alumnado
from callbacks.alumnado.graphs.personal.callback_graph_progreso_academico_alumnado import update_graph_alumnado
from callbacks.alumnado.graphs.personal.callback_graph_calif_numerica_alumnado import update_graph_alumnado
from callbacks.alumnado.graphs.personal.callback_graph_tasa_exito_alumnado import update_graph_alumnado

def graphs_personal_alumnado():
  return html.Div([
    html.Div([
      dcc.Graph(
          id='graph-evolucion-progreso-academico',
          figure={},
    )], className='graph-item'),
    html.Div([
      dcc.Graph(
          id='graph-bar-evolucion-asignaturas-matriculadas',
          figure={}
    )], className='graph-item'),
    html.Div([
      dcc.Graph(
          id='graph-bar-calificaciones-por-asignatura',
          figure={}
    )], className='graph-item'),
    html.Div([
      dcc.Graph(
          id='graph-bar-tasa-exito',
          figure={}
    )], className='graph-item')
  ], className='graphs-container')            
  
