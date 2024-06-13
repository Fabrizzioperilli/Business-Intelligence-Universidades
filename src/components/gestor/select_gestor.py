from dash import html, dcc
from callbacks.gestor.callback_select_gestor import store_selected_gestor

def select_gestor():
      return html.Div([
          html.Div([
              dcc.Dropdown(
                  options=[],
                  value=None,
                  id='gestor-dropdown',
                  clearable=False
              )
          ], className='select-gestor'),
      ])