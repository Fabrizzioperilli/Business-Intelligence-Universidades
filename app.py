from dash import dash, html
import components.common.header as header
import components.common.footer as footer
from layouts.alumno_layout import alumno_layout
from layouts.docente_layout import docente_layout
from layouts.gestor_layout import gestor_layout
from callbacks.common.callback_update_layout import update_layout
from callbacks.alumnado.callback_select_alumnado import store_selected_alumnado
from data.db_connector import db 
import atexit

# Crear la aplicación Dash
app = dash.Dash(
    __name__, 
    external_stylesheets=[
        'assets/css/styles.css',
        'https://cdn-uicons.flaticon.com/2.3.0/uicons-thin-rounded/css/uicons-thin-rounded.css'
    ], 
    suppress_callback_exceptions=True
)

app.title = 'Dashboard académico Ull'
app._favicon = 'assets/images/favicon.ico'
server = app.server

app.layout = html.Div([
    header.Header(store_id='store-role'),
    html.Div(id='page-content'),
    footer.Footer(),
])

#Cierre de la conexión a la base de datos
atexit.register(db.close)

# Iniciar el servidor
if __name__ == '__main__':
    app.run_server(debug=True)
