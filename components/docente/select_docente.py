from dash import html, dcc
from data.db_connector import db
from callbacks.docente.callback_select_docente import store_selected_docente

def select_docente():
    query = "SELECT DISTINCT id_docente FROM docentes"
    result = db.execute_query(query)
    opciones_dropdown = [{'label': alumno[0], 'value': alumno[0]} for alumno in result]
    
    return html.Div([
        html.Div([
            dcc.Dropdown(
                options=opciones_dropdown,
                value=None,
                id='docente-dropdown',
                clearable=False
            )
        ], className='select-docente'),
    ]) 