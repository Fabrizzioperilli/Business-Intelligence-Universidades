from dash import dash, html
import components.common.header as header
import components.common.footer as footer
from layouts.alumno_layout import alumno_layout
from layouts.docente_layout import docente_layout
from layouts.gestor_layout import gestor_layout
from callbacks.common.callback_update_layout import update_layout
from data.db_connector import db 
import atexit
import dash_bootstrap_components as dbc


app = dash.Dash(
    __name__, 
    external_stylesheets=[
        'src/assets/css/styles.css',
        dbc.themes.BOOTSTRAP
    ], 
    suppress_callback_exceptions=True
)

app.title = 'Dashboard académico'
app._favicon = 'src/assets/images/favicon.ico'
server = app.server

app.layout = html.Div([
    header.header('store-role'),
    html.Div(id='page-content'),
    footer.footer(),
])

#Cierre de la conexión a la base de datos
atexit.register(db.close)

# Iniciar el servidor
if __name__ == '__main__':
    app.run_server(debug=True)
