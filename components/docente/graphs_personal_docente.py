from dash import html, dcc
from callbacks.docente.graphs.personal.callback_graph_alu_repetidores_nuevos_docente import update_graph_docente
from callbacks.docente.graphs.personal.callback_graph_alu_genero_docente import update_graph_docente
from callbacks.docente.graphs.personal.callback_graph_alu_media_docente import update_graph_docente
from callbacks.docente.graphs.personal.callback_graph_alu_nota_cualitativa_docente import update_graph_docente

def graphs_personal_docente():
  return html.Div([
    html.Div([
      dcc.Graph(
          id='graph-alumnos-repetidores-nuevos',
          figure={},
    )], className='graph-item-personal-docente'),
    html.Div([
      dcc.Graph(
          id='graph-alumnos-matri-genero',
          figure={}
    )], className='graph-item-personal-docente'),
    html.Div([
      dcc.Graph(
          id='graph-alumnos-nota-media',
          figure={},
    )], className='graph-item-personal-docente'),
    html.Div([
      dcc.Graph(
          id='graph-alumnos-nota-cualitativa',
          figure={}
    )], className='graph-item-personal-docente')
  ], className='graphs-container-personal-docente')