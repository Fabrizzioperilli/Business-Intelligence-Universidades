from dash import html, dcc
from callbacks.docente.graphs.personal.callback_graph_alu_repetidores_nuevos_docente import update_graph_docente
from callbacks.docente.graphs.personal.callback_graph_alu_genero_docente import update_graph_docente
from callbacks.docente.graphs.personal.callback_graph_alu_media_docente import update_graph_docente

def graphs_personal_docente():
  return html.Div([
    html.Div([
      dcc.Graph(
          id='graph-alumnos-repetidores-nuevos',
          figure={},
    )], className='graph-item'),
    html.Div([
      dcc.Graph(
          id='graph-alumnos-matri-genero',
          figure={}
    )], className='graph-item'),
    html.Div([
      dcc.Graph(
          id='graph-alumnos-nota-media',
          figure={},
    )], className='graph-item'),
    html.Div([
      dcc.Graph(
          id='',
          figure={}
    )], className='graph-item')
  ], className='graphs-container-docente')