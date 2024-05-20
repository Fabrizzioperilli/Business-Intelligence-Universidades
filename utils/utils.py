from data.queries import nota_media_alumno_titulacion
import random

#Función para calcular la media de los alumnos
def calculate_average_grade(alumno_id, titulacion):
    result = nota_media_alumno_titulacion(alumno_id, titulacion)
    
    if result and result[0][0] is not None:
        return round(result[0][0], 2)
    else:
        return "No disponible"
    
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
    