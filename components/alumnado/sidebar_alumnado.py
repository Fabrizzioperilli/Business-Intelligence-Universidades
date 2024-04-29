from dash import html
import components.alumnado.resumen_alumnado as resumen_alumnado
import components.alumnado.filters_alumnado as filters_alumnado

def sidebar_alumnado():
    return html.Div([
      resumen_alumnado.resumen_alumnado(),
      filters_alumnado.filters_alumnado(),
    ], className='sidebar')
  
      
  