from dash import html, dcc
from callbacks.gestor.graphs.riesgo_abandono.callback_graph_tasa_abandono_gestor import update_graph_gestor
from callbacks.gestor.graphs.riesgo_abandono.callback_graph_tasa_graduacion_gestor import update_graph_gestor
from components.common.modal_data import create_modal

def graphs_riesgo_abandono_gestor():
  return html.Div([
      html.Div([
            dcc.Loading(
                children=[
                    dcc.Graph(
                        id='tasa-abandono-gestor',
                        figure={},
                    )
                ]
            ),
            create_modal(
                'modal-tasa-abandono', 
                'table-container-tasa-abandono', 
                'btn-descargar-tasa-abandono', 
                'btn-ver-datos-tasa-abandono'
            ),
        ], className='graph-item-riesgo-abandono-gestor'),
    html.Div([
      dcc.Loading(
          children=[
              dcc.Graph(
                  id='tasa-graduacion-gestor',
                  figure={}
              ),
          ]
      ),
      create_modal('modal-tasa-graduacion', 
                  'table-container-tasa-graduacion', 
                  'btn-descargar-tasa-graduacion', 
                  'btn-ver-datos-tasa-graduacion'),
    ], className='graph-item-riesgo-abandono-gestor'),
  ], className='graphs-container-riesgo-abandono-gestor')