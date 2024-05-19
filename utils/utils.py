from data.db_connector import db

def calculate_average_grade(alumno_id, titulacion):
    query = """
    SELECT AVG(li.calif_numerica) AS media_calif
    FROM public.lineas_actas li
    JOIN public.matricula m ON m.id = li.id AND m.cod_plan = li.cod_plan
    WHERE li.id = :alumno_id
    AND li.calif_numerica >= 5 
    AND m.titulacion = :titulacion;
    """
    result = db.execute_query(query, {'alumno_id': alumno_id, 'titulacion': titulacion})
    
    if result and result[0][0] is not None:
        return round(result[0][0], 2)
    else:
        return "No disponible"
    

def list_to_tuple(value):
    if isinstance(value, str):
        return (value,)
    elif isinstance(value, list):
        return tuple(value)
    else:
        return ValueError("Tipo de dato no soportado, se esperaba un list o str. {}".format(type(value)))