from data.db_connector import db
from data.queries_dictionary import queries
from functools import lru_cache


# Función para comprobar si la query se ha ejecutado correctamente
def check_data(query, params):
    try:
        data = db.execute_query(query, params)
    except Exception as e:
        print("Query execution failed: ", e)
        return []
    return data


# Decorador para cachear las queries y evitar hacer consultas innecesarias
def cache_query(func):
    @lru_cache(maxsize=32)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


@cache_query
def alumnos_all():
    query = queries["alumnado"]["common"]["alumnos_all"]
    return check_data(query, {})


@cache_query
def resumen_alumno(alumno_id, titulacion):
    query = queries["alumnado"]["common"]["resumen_alumno"]
    params = {"alumno_id": alumno_id, "titulacion": titulacion}

    return check_data(query, params)


@cache_query
def resumen_gestor(gestor_id):
    query = queries["gestor"]["common"]["resumen_gestor"]
    params = {"gestor_id": gestor_id}

    return check_data(query, params)


@cache_query
def nota_media_alumno_titulacion(alumno_id, titulacion):
    query = queries["alumnado"]["common"]["nota_media_alumno_titulacion"]
    params = {"alumno_id": alumno_id, "titulacion": titulacion}

    data = check_data(query, params)

    if not data:
        return "No disponible"

    return round(data[0][0], 2)


@cache_query
def curso_academico_alumnado(alumno_id, titulacion):
    query = queries["alumnado"]["filters"]["curso_academico_alumnado"]
    params = {"alumno_id": alumno_id, "titulacion": titulacion}

    return check_data(query, params)


@cache_query
def asignaturas_matriculadas(alumno_id, curso_academico, titulacion):
    query = queries["alumnado"]["filters"]["asinaturas_matriculadas"]
    params = {
        "alumno_id": alumno_id,
        "curso_academico": curso_academico,
        "titulacion": titulacion,
    }

    return check_data(query, params)


@cache_query
def titulacion_alumnado(alumno_id):
    query = queries["alumnado"]["filters"]["titulacion_alumnado"]
    params = {"alumno_id": alumno_id}

    return check_data(query, params)


@cache_query
def asignaturas_superadas(alumno_id, curso_academico, titulacion):
    query = queries["alumnado"]["graphs"]["personal"][
        "curso_academico_asignaturas_superadas"
    ]
    params = {
        "alumno_id": alumno_id,
        "curso_academico": curso_academico,
        "titulacion": titulacion,
    }

    return check_data(query, params)


@cache_query
def calif_cualitativa_asignatura(alumno_id, curso_academico, titulacion):
    query = queries["alumnado"]["graphs"]["personal"]["calif_cualitativa_asginatura"]
    params = {
        "alumno_id": alumno_id,
        "curso_academico": curso_academico,
        "titulacion": titulacion,
    }

    return check_data(query, params)


@cache_query
def calif_numerica_asignatura(alumno_id, curso_academico, titulacion):
    query = queries["alumnado"]["graphs"]["personal"]["calif_numerica_asignatura"]
    params = {
        "alumno_id": alumno_id,
        "curso_academico": curso_academico,
        "titulacion": titulacion,
    }

    return check_data(query, params)


@cache_query
def asignaturas_matriculadas_y_superadas(alumno_id, curso_academico, titulacion):
    query = queries["alumnado"]["graphs"]["personal"][
        "asignaturas_matriculadas_y_superadas"
    ]
    params = {
        "alumno_id": alumno_id,
        "curso_academico": curso_academico,
        "titulacion": titulacion,
    }

    return check_data(query, params)


@cache_query
def asignaturas_superadas_media_abandono(
    curso_academico, asignaturas_matriculadas, titulacion, cod_universidad
):
    query = queries["alumnado"]["graphs"]["general"][
        "asignaturas_superadas_media_abandono"
    ]
    params = {
        "curso_academico": curso_academico,
        "asignaturas_matriculadas": asignaturas_matriculadas,
        "titulacion": titulacion,
        "cod_universidad": cod_universidad,
    }

    return check_data(query, params)


@cache_query
def calif_cualitativa_comparativa(
    curso_academico, asignaturas_matriculadas, titulacion, cod_universidad
):
    query = queries["alumnado"]["graphs"]["general"]["calif_cualitativa_comparativa"]
    params = {
        "curso_academico": curso_academico,
        "asignaturas_matriculadas": asignaturas_matriculadas,
        "titulacion": titulacion,
        "cod_universidad": cod_universidad,
    }

    return check_data(query, params)


@cache_query
def calif_cualitativa_alumno_asignaturas(
    alumno_id, curso_academico, asignaturas_matriculadas, titulacion
):
    query = queries["alumnado"]["graphs"]["general"][
        "calif_cualitativa_alumno_asignaturas"
    ]
    params = {
        "alumno_id": alumno_id,
        "curso_academico": curso_academico,
        "asignaturas_matriculadas": asignaturas_matriculadas,
        "titulacion": titulacion,
    }

    return check_data(query, params)


@cache_query
def nota_media_general_mi_nota(
    curso_academico, asignaturas_matriculadas, alumno_id, titulacion, cod_universidad
):
    query = queries["alumnado"]["graphs"]["general"]["nota_media_general_mi_nota"]
    params = {
        "curso_academico": curso_academico,
        "asignaturas_matriculadas": asignaturas_matriculadas,
        "alumno_id": alumno_id,
        "titulacion": titulacion,
        "cod_universidad": cod_universidad,
    }

    return check_data(query, params)


@cache_query
def alumnos_repetidores_nuevos(docente_id, curso_academico, asignaturas):
    query = queries["docente"]["graphs"]["personal"]["alumnos_repetidores_nuevos"]
    params = {
        "docente_id": docente_id,
        "curso_academico": curso_academico,
        "asignaturas": asignaturas,
    }

    return check_data(query, params)


@cache_query
def asignaturas_docente(id_docente, titulacion):
    query = queries["docente"]["filters"]["asignaturas_docente"]
    params = {"id_docente": id_docente, "titulacion": titulacion}

    return check_data(query, params)


@cache_query
def curso_academico_docente(id_docente, asignatura):
    query = queries["docente"]["filters"]["curso_academico_docente"]
    params = {"id_docente": id_docente, "asignatura": asignatura}

    return check_data(query, params)


@cache_query
def titulacion_docente(id_docente):
    query = queries["docente"]["filters"]["titulacion_docente"]
    params = {"id_docente": id_docente}

    return check_data(query, params)


@cache_query
def resumen_docente(id_docente, titulacion):
    query = queries["docente"]["common"]["resumen_docente"]
    params = {"id_docente": id_docente, "titulacion": titulacion}

    return check_data(query, params)


@cache_query
def docentes_all():
    query = queries["docente"]["common"]["docentes_all"]
    return check_data(query, {})


@cache_query
def alumnos_genero_docente(id_docente, asignaturas, curso_academico):
    query = queries["docente"]["graphs"]["personal"]["alumnos_genero_docente"]
    params = {
        "id_docente": id_docente,
        "asignaturas": asignaturas,
        "curso_academico": curso_academico,
    }

    return check_data(query, params)


@cache_query
def alumnos_nota_media_docente(asignaturas, curso_academico):
    query = queries["docente"]["graphs"]["personal"]["alumnos_nota_media_docente"]
    params = {"asignaturas": asignaturas, "curso_academico": curso_academico}

    return check_data(query, params)


@cache_query
def alumnos_nota_cualitativa_docente(asignaturas, curso_academico):
    query = queries["docente"]["graphs"]["personal"]["alumnos_nota_cualitativa_docente"]
    params = {"asignaturas": asignaturas, "curso_academico": curso_academico}

    return check_data(query, params)


@cache_query
def curso_academico_actas_titulacion(titulacion):
    query = queries["docente"]["filters"]["curso_academico_actas_titulacion"]
    params = {"titulacion": titulacion}

    return check_data(query, params)


@cache_query
def asignaturas_actas_titulacion(titulacion, curso_academico):
    query = queries["docente"]["filters"]["asignaturas_actas_titulacion"]
    params = {"titulacion": titulacion, "curso_academico": curso_academico}

    return check_data(query, params)


@cache_query
def calif_all_cualitativa_asignaturas(titulacion, curso_academico, asignaturas):
    query = queries["docente"]["graphs"]["general"]["calif_all_cualitativa_asignaturas"]
    params = {
        "titulacion": titulacion,
        "curso_academico": curso_academico,
        "asignaturas": asignaturas,
    }

    return check_data(query, params)


@cache_query
def calif_media_asignaturas(titulacion, curso_academico, asignaturas):
    query = queries["docente"]["graphs"]["general"]["calif_media_asignaturas"]
    params = {
        "titulacion": titulacion,
        "curso_academico": curso_academico,
        "asignaturas": asignaturas,
    }

    return check_data(query, params)


@cache_query
def gestores_all():
    query = queries["gestor"]["common"]["gestores_all"]
    return check_data(query, {})


@cache_query
def numero_alumnos_matriculados_universidad(universidad):
    query = queries["gestor"]["common"]["numero_alumnos_matriculados_universidad"]
    params = {"universidad": universidad}

    return check_data(query, params)


@cache_query
def universidades_gestor(gestor_id):
    query = queries["gestor"]["common"]["universidades_gestor"]
    params = {"gestor_id": gestor_id}

    return check_data(query, params)


@cache_query
def curso_academico_universidad(cod_universidad):
    query = queries["gestor"]["filters"]["curso_academico_universidad"]
    params = {"cod_universidad": cod_universidad}

    return check_data(query, params)


@cache_query
def titulaciones_universidad_gestor(cod_universidad, curso_academico):
    query = queries["gestor"]["filters"]["titulaciones_universidad_gestor"]
    params = {"cod_universidad": cod_universidad, "curso_academico": curso_academico}

    return check_data(query, params)


@cache_query
def alumnos_nuevo_ingreso_genero_titulacion(
    curso_academico, titulaciones, cod_universidad
):
    query = queries["gestor"]["graphs"]["indicadores"][
        "alumnos_nuevo_ingreso_genero_titulacion"
    ]
    params = {
        "curso_academico": curso_academico,
        "titulaciones": titulaciones,
        "cod_universidad": cod_universidad,
    }

    return check_data(query, params)


@cache_query
def alumnos_egresados_genero_titulacion(cod_universidad, curso_academico, titulaciones):
    query = queries["gestor"]["graphs"]["indicadores"][
        "alumnos_egresados_genero_titulacion"
    ]
    params = {
        "cod_universidad": cod_universidad,
        "curso_academico": curso_academico,
        "titulaciones": titulaciones,
    }

    return check_data(query, params)


@cache_query
def alumnos_egresados_nacionalidad_titulacion(
    cod_universidad, curso_academico, titulaciones
):
    query = queries["gestor"]["graphs"]["indicadores"][
        "alumnos_egresados_nacionalidad_titulacion"
    ]
    params = {
        "cod_universidad": cod_universidad,
        "curso_academico": curso_academico,
        "titulaciones": titulaciones,
    }

    return check_data(query, params)


@cache_query
def alumnos_nuevo_ingreso_nacionalidad_titulacion(
    cod_universidad, curso_academico, titulaciones
):
    query = queries["gestor"]["graphs"]["indicadores"][
        "alumnos_nuevo_ingreso_nacionalidad_titulacion"
    ]
    params = {
        "cod_universidad": cod_universidad,
        "curso_academico": curso_academico,
        "titulaciones": titulaciones,
    }

    return check_data(query, params)


@cache_query
def nota_media_acceso_titulacion(cod_universidad):
    query = queries["gestor"]["graphs"]["resultados"]["nota_media_acceso_titulacion"]
    params = {"cod_universidad": cod_universidad}

    return check_data(query, params)


@cache_query
def duracion_media_estudios_nota_gestor(cod_universidad):
    query = queries["gestor"]["graphs"]["resultados"][
        "duracion_media_estudios_nota_gestor"
    ]
    params = {"cod_universidad": cod_universidad}

    return check_data(query, params)


@cache_query
def cursos_academicos_egresados(cod_universidad):
    query = queries["gestor"]["common"]["cursos_academicos_de_egresados"]
    params = {"cod_universidad": cod_universidad}

    return check_data(query, params)


@cache_query
def tasa_abandono_titulacion_gestor(cod_universidad, curso_academico):
    query = queries["gestor"]["graphs"]["riesgo_abandono"][
        "tasa_abandono_titulacion_gestor"
    ]
    params = {"cod_universidad": cod_universidad, "curso_academico": curso_academico}

    return check_data(query, params)


@cache_query
def tasa_graduacion_titulacion_gestor(cod_universidad, curso_academico):
    query = queries["gestor"]["graphs"]["riesgo_abandono"][
        "tasa_graduacion_titulacion_gestor"
    ]
    params = {"cod_universidad": cod_universidad, "curso_academico": curso_academico}

    return check_data(query, params)


@cache_query
def universidad_alumno(alumno_id):
    query = queries["alumnado"]["common"]["universidad_alumno"]
    params = {"alumno_id": alumno_id}

    return check_data(query, params)


@cache_query
def universidades_docente(id_docente):
    query = queries["docente"]["common"]["universidades_docente"]
    params = {"id_docente": id_docente}

    return check_data(query, params)
