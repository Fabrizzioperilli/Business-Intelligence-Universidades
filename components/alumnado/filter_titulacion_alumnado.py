from dash import html, dcc
from callbacks.alumnado.callback_filter_titulacion_alumnado import update_filter_titulacion_alumnado


def filter_titulacion_alumnado():
    return html.Div([
        html.Label("Titulación"),
        dcc.Dropdown(
          id='titulacion-alumnado',
          options=[],
          value=None,
          searchable=False,
          clearable=False,
          optionHeight=50,
          maxHeight=300,
        ),
        html.Br()
    ])