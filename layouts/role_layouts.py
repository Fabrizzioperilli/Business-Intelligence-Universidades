
from dash import html

# Define layout functions for each role
def alumno_layout():
    return html.Div([
        html.H2("Alumno Dashboard", className='dashboard-title'),
    ])

def docente_layout():
    return html.Div([
        html.H2("Docente Dashboard", className='dashboard-title'),
    ])

def gestor_layout():
    return html.Div([
        html.H2("Gestor Dashboard", className='dashboard-title'),
    ])
