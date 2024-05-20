
from data.db_connector import db
from data.queries_dictionary import queries


def check_data(query, params):
    try:
        data = db.execute_query(query, params)
    except Exception as e:
        print("Query execution failed: ", e)
        return []
    return data

    
def alumnos_all():
    query = queries['alumnado']['common']['alumnos_all']
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

def asignaturas_superadas(alumno_id, curso_academico, titulacion):
    query = queries['alumnado']['graphs']['personal']['curso_academico_asignaturas_superadas']
    params = {'alumno_id': alumno_id, 
              'curso_academico': curso_academico, 
              'titulacion': titulacion}

    return check_data(query, params)

def calif_cualitativa_asignatura(alumno_id, curso_academico, titulacion):
    query = queries['alumnado']['graphs']['personal']['calif_cualitativa_asginatura']
    params = {'alumno_id': alumno_id, 
              'curso_academico': curso_academico, 
              'titulacion': titulacion}

    return check_data(query, params)

def calif_numerica_asignatura(alumno_id, curso_academico, titulacion):
    query = queries['alumnado']['graphs']['personal']['calif_numerica_asignatura']
    params = {'alumno_id': alumno_id, 
              'curso_academico': curso_academico, 
              'titulacion': titulacion}

    return check_data(query, params)

def asignaturas_matriculadas_y_superadas(alumno_id, curso_academico, titulacion):
    query = queries['alumnado']['graphs']['personal']['asignaturas_matriculadas_y_superadas']
    params = {'alumno_id': alumno_id, 
              'curso_academico': curso_academico, 
              'titulacion': titulacion}

    return check_data(query, params)
        
def asignaturas_superadas_media_abandono(curso_academico, asignaturas_matriculadas, titulacion):
    query = queries['alumnado']['graphs']['general']['asignaturas_superadas_media_abandono']
    params = {'curso_academico': curso_academico, 
              'asignaturas_matriculadas': asignaturas_matriculadas, 
              'titulacion': titulacion}

    return check_data(query, params)

def calif_cualitativa_comparativa(curso_academico, asignaturas_matriculadas, titulacion):
    query = queries['alumnado']['graphs']['general']['calif_cualitativa_comparativa']
    params = {'curso_academico': curso_academico, 
              'asignaturas_matriculadas': asignaturas_matriculadas,
              'titulacion': titulacion}

    return check_data(query, params)

def calif_cualitativa_alumno_asignaturas(alumno_id, curso_academico, asignaturas_matriculadas, titulacion):
    query = queries['alumnado']['graphs']['general']['calif_cualitativa_alumno_asignaturas']
    params = {'alumno_id': alumno_id,
              'curso_academico': curso_academico, 
              'asignaturas_matriculadas': asignaturas_matriculadas,
              'titulacion': titulacion}
    
    return check_data(query, params)

def nota_media_general_mi_nota(curso_academico, asignaturas_matriculadas, alumno_id, titulacion):
    query = queries['alumnado']['graphs']['general']['nota_media_general_mi_nota']
    params = {'curso_academico': curso_academico, 
              'asignaturas_matriculadas': asignaturas_matriculadas, 
              'alumno_id': alumno_id,
              'titulacion': titulacion}

    return check_data(query, params)

def alumnos_repetidores_nuevos(docente_id, curso_academico, asignaturas):
    query = queries['docente']['graphs']['personal']['alumnos_repetidores_nuevos']
    params = {'docente_id': docente_id,
              'curso_academico': curso_academico,
              'asignaturas': asignaturas}

    return check_data(query, params)


def asignaturas_docente(id_docente, titulacion):
    query = queries['docente']['filters']['asignaturas_docente']
    params = {'id_docente': id_docente, 'titulacion': titulacion}

    return check_data(query, params)


def curso_academico_docente(id_docente, asignatura):
    query = queries['docente']['filters']['curso_academico_docente']
    params = {'id_docente': id_docente, 'asignatura': asignatura}

    return check_data(query, params)


def titulacion_docente(id_docente):
    query = queries['docente']['filters']['titulacion_docente']
    params = {'id_docente': id_docente}

    return check_data(query, params)
    

def resumen_docente(id_docente, titulacion):
    query = queries['docente']['common']['resumen_docente']
    params = {'id_docente': id_docente, 'titulacion': titulacion}

    return check_data(query, params)


def docentes_all():
    query = queries['docente']['common']['docentes_all']
    return check_data(query, {})

def alumnos_genero_docente(id_docente, asignaturas, curso_academico):
    query = queries['docente']['graphs']['personal']['alumnos_genero_docente']
    params = {'id_docente': id_docente, 
              'asignaturas': asignaturas, 
              'curso_academico': curso_academico}

    return check_data(query, params)


def alumnos_nota_media_docente(asignaturas, curso_academico):
    query = queries['docente']['graphs']['personal']['alumnos_nota_media_docente']
    params = {'asignaturas': asignaturas, 
              'curso_academico': curso_academico}

    return check_data(query, params)


def alumnos_nota_cualitativa_docente(asignaturas, curso_academico):
    query = queries['docente']['graphs']['personal']['alumnos_nota_cualitativa_docente']
    params = {'asignaturas': asignaturas, 
              'curso_academico': curso_academico}

    return check_data(query, params)


def curso_academico_actas_titulacion(titulacion):
    query = queries['docente']['filters']['curso_academico_actas_titulacion']
    params = {'titulacion': titulacion}

    return check_data(query, params)


def asignaturas_actas_titulacion(titulacion, curso_academico):
    query = queries['docente']['filters']['asignaturas_actas_titulacion']
    params = {'titulacion': titulacion, 'curso_academico': curso_academico}

    return check_data(query, params)