
from data.db_connector import db
from data.queries_dictionary import queries


def check_data(query, params):
    try:
        data = db.execute_query(query, params)
    except Exception as e:
        print("Query execution failed: ", e)
        return []
    return data

    
def alumnos():
    query = queries['alumnado']['common']['alumnos']
    return check_data(query, {})

def resumen_alumno(alumno_id, titulacion):
    query = queries['alumnado']['common']['resumen_alumno']
    params = {'alumno_id': alumno_id, 'titulacion': titulacion}
    
    return check_data(query, params)

def nota_media_alumno_titulacion(alumno_id, titulacion):
    query = queries['alumnado']['common']['nota_media_alumno_titulacion']
    params = {'alumno_id': alumno_id, 'titulacion': titulacion}
    
    return check_data(query, params)

def curso_academico_alumnado(alumno_id, titulacion):
    query = queries['alumnado']['filters']['curso_academico_alumnado']
    params = {'alumno_id': alumno_id, 'titulacion': titulacion}

    return check_data(query, params)


def asignaturas_matriculadas(alumno_id, curso_academico, titulacion):
    query = queries['alumnado']['filters']['asinaturas_matriculadas']
    
    params = {'alumno_id': alumno_id, 
              'curso_academico': curso_academico, 
              'titulacion': titulacion}

    return check_data(query, params)

def titulacion_alumnado(alumno_id):
    query = queries['alumnado']['filters']['titulacion_alumnado']
    params = {'alumno_id': alumno_id}

    return check_data(query, params)
        
    