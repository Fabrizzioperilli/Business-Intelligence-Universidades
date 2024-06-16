import random

#Función para convertir una lista en una tupla
def list_to_tuple(value):
    if isinstance(value, str):
        return (value,)
    elif isinstance(value, list):
        return tuple(value)
    else:
        return ValueError("Tipo de dato no soportado, se esperaba un list o str. {}".format(type(value)))
    
#Función para generar colores aleatorios
def random_color(size):
    return ['#%06X' % random.randint(0, 0xFFFFFF) for _ in range(size)]
    

config_mode_bar_buttons_gestor = {
        'displayModeBar': True,
        'displaylogo': False,
        'scrollZoom': True,
        'modeBarButtonsToRemove': ['zoom2d', 'lasso2d', 'resetScale2d'],
        'modeBarButtonsToAdd': [
            'drawline',
            'drawcircle',
            'drawrect',
            'eraseshape',
            'toggleSpikelines',
        ]
    }