import random


# Función para convertir una lista en una tupla
def list_to_tuple(value):
    """
    Función para convertir una lista en una tupla
    :param value: Lista a convertir
    :return: Tupla
    """
    if isinstance(value, str):
        return (value,)
    elif isinstance(value, list):
        return tuple(value)
    else:
        return ValueError(
            "Tipo de dato no soportado, se esperaba un list o str. {}".format(
                type(value)
            )
        )


def random_color(size):
    """
    Función para generar colores aleatorios en formato hexadecimal
    :param size: Número de colores a generar
    :return: Lista de colores en formato hexadecimal
    """
    return ["#%06X" % random.randint(0, 0xFFFFFF) for _ in range(size)]


# Configuración de los botones de la barra de herramientas de Plotly
config_mode_bar_buttons_gestor = {
    "displayModeBar": True,
    "displaylogo": False,
    "scrollZoom": True,
    "modeBarButtonsToRemove": ["zoom2d", "lasso2d", "resetScale2d"],
    "modeBarButtonsToAdd": [
        "drawline",
        "drawcircle",
        "drawrect",
        "eraseshape",
        "toggleSpikelines",
    ],
}
