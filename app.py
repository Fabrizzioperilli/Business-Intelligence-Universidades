import dash
from dash import dcc, html, Input, Output
import components.common.header as header
import components.common.footer as footer
from layouts.alumno_layout import alumno_layout
from layouts.docente_layout import docente_layout
from layouts.gestor_layout import gestor_layout

app = dash.Dash(__name__, external_stylesheets=['assets/css/styles.css', 'https://cdn-uicons.flaticon.com/2.3.0/uicons-thin-rounded/css/uicons-thin-rounded.css'], suppress_callback_exceptions=True)
app.title = 'Dashboard ULL'
app._favicon = 'assets/images/favicon.ico'
server = app.server

# Define the layout for the Dash application, which includes the header, main content, and footer.
app.layout = html.Div([
    header.Header(store_id='store-role'),  # Asegúrate que este ID es el que se usa en los callbacks
    html.Div(id='page-content'),  # Placeholder para el contenido principal de la página
    footer.Footer(),  # Componente Footer
])

# Callback to dynamically change the layout based on the role selected by the user
@app.callback(
    Output('page-content', 'children'),
    [Input('store-role', 'data')]
)
def update_layout(role):
    if role == 'Alumno':
        layout = alumno_layout()
    elif role == 'Docente':
        layout = docente_layout()
    elif role == 'Gestor':
        layout = gestor_layout()
    return layout

# Start the server if this file is executed directly, useful for local development.
if __name__ == '__main__':
    app.run_server(debug=True)