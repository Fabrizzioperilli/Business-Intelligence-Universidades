from dash import html, dcc, callback, Output, Input
from data.db_connector import db
from callbacks.alumnado.callback_select_alumnado import store_selected_alumnado

def select_alumnado():
    query = "SELECT id FROM alumnos"
    result = db.execute_query(query)
    opciones_dropdown = [{'label': alumno[0], 'value': alumno[0]} for alumno in result]
    
    return html.Div([
        html.Div([
            dcc.Dropdown(
                options=opciones_dropdown,
                value=None,
                id='alumnado-dropdown',
                clearable=False
            )
        ], className='select-alumnado'),
    ]) 
