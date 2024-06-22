#
# @file generate_synthetic_data.py
# @brief Este archivo contiene el código para generar datos sintéticos.
# @details Se generan datos sintéticos para las tablas de la base de datos.
# @version 1.0
# @date 12/06/2024
# @license MIT License
# @author Fabrizzio Daniell Perilli Martín
# @email alu0101138589@ull.edu.es
#

import pandas as pd
import numpy as np
from faker import Faker
import random
from tqdm import tqdm
import os

fake = Faker('es_ES')

# Diccionario con ramas, titulaciones y palabras clave
educacion = {
    'Ingeniería y Tecnología': {
        'Ingeniería Informática': [
            'Programación', 'Algoritmos', 'Estructuras de Datos', 'Bases de Datos', 'Sistemas Operativos',
            'Redes', 'Inteligencia Artificial', 'Seguridad Informática', 'Desarrollo Web', 'Software',
            'Ciberseguridad', 'Ingeniería del Software', 'Bases de Datos Avanzadas', 'Arquitectura de Computadoras',
            'Gráficos por Computadora', 'Desarrollo de Aplicaciones', 'Computación en la Nube', 'Blockchain',
            'Big Data', 'Analítica de Datos', 'Aprendizaje Automático', 'Computación Paralela', 'Ciencias de la Computación',
            'Tecnologías de la Información', 'Interacción Humano-Computadora', 'Teoría de la Computación', 'Robótica',
            'Computación Cuántica', 'Sistemas Embebidos', 'Desarrollo de Videojuegos', 'Visión por Computador',
            'Minería de Datos', 'Internet de las Cosas', 'Bioinformática', 'Sistemas Distribuidos', 'Cómputo de Alto Rendimiento',
            'Cálculo Numérico', 'Realidad Virtual', 'Realidad Aumentada'
        ]
    },
    'Ciencias de la Salud': {
        'Medicina': [
            'Anatomía', 'Fisiología', 'Bioquímica', 'Farmacología', 'Patología',
            'Genética', 'Neurología', 'Cardiología', 'Cirugía', 'Dermatología',
            'Endocrinología', 'Epidemiología', 'Gastroenterología', 'Ginecología',
            'Hematología', 'Infectología', 'Medicina Interna', 'Nefrología',
            'Neumología', 'Oncología', 'Pediatría', 'Psiquiatría', 'Radiología',
            'Reumatología', 'Urología', 'Medicina Familiar', 'Medicina Preventiva',
            'Emergencias Médicas', 'Cuidados Intensivos', 'Medicina Deportiva', 'Medicina Nuclear',
            'Oftalmología', 'Otorrinolaringología', 'Rehabilitación', 'Medicina del Trabajo',
            'Medicina Forense', 'Geriatría', 'Inmunología', 'Toxicología', 'Anestesiología',
            'Nutriología', 'Microbiología', 'Parasitología', 'Patología Clínica', 'Genómica',
            'Neurocirugía'
        ]
    },
    'Ciencias Sociales y Jurídicas': {
        'Derecho': [
            'Derecho Civil', 'Derecho Penal', 'Derecho Constitucional', 'Derecho Administrativo', 'Derecho Laboral',
            'Derecho Mercantil', 'Derecho Internacional', 'Derecho Tributario', 'Derecho Ambiental', 'Derecho de Familia',
            'Derecho Procesal', 'Derecho Romano', 'Derecho Comparado', 'Derecho Financiero', 'Derecho Agrario',
            'Derecho Informático', 'Derecho de la Competencia', 'Derecho de la Propiedad Intelectual', 'Derecho Bancario',
            'Derecho Marítimo', 'Derecho Aéreo', 'Derecho del Consumo', 'Derecho de la Seguridad Social', 'Derecho Minero',
            'Derecho de la Energía', 'Derecho Urbanístico', 'Derecho de la Salud', 'Derecho del Deporte', 'Derecho de las Telecomunicaciones',
            'Derecho Internacional Privado', 'Derecho Internacional Público', 'Derecho de la Unión Europea', 'Derecho Canónico',
            'Derecho Militar', 'Derecho Electoral', 'Derecho Humanitario', 'Derecho Notarial', 'Derecho Penitenciario',
            'Derecho Registral'
        ]
    },
    'Humanidades': {
        'Historia': [
            'Historia Antigua', 'Historia Medieval', 'Historia Moderna', 'Historia Contemporánea', 'Historia de América',
            'Historia de Europa', 'Historia de Asia', 'Historia de África', 'Historia de Oceanía', 'Historia del Arte',
            'Historia Económica', 'Historia Política', 'Historia Social', 'Historiografía', 'Historia de la Ciencia',
            'Arqueología', 'Historia Militar', 'Historia de las Religiones', 'Historia Cultural', 'Historia de las Ideas',
            'Teoría de la Historia', 'Métodos de Investigación Histórica', 'Historia de la Educación', 'Historia de la Mujer',
            'Historia Ambiental', 'Historia Oral', 'Historia de la Tecnología', 'Historia Urbana', 'Historia de la Salud'
        ]
    }
}

# Diccionario de universidades con su código correspondiente
universidades_dict = {
    'Universidad de Madrid': 'UDM01',
    'Universidad de Barcelona': 'UDB02',
    'Universidad de La Laguna': 'ULL03',
}


def generate_asignaturas(educacion, min_asignaturas=38):
    """
    Genera un diccionario con asignaturas aleatorias para cada titulación.
    
    Args:
        educacion (dict): Diccionario con ramas, titulaciones y palabras clave.
        min_asignaturas (int): Número mínimo de asignaturas por titulación.
        
    Returns:
        dict: Diccionario con asignaturas para cada titulación.
    """
    asignaturas_dict = {}
    for rama, titulaciones in educacion.items():
        for titulacion, palabras in titulaciones.items():
            num_asignaturas = min(min_asignaturas, len(palabras))
            asignaturas = random.sample(palabras, num_asignaturas)
            asignaturas_dict[titulacion] = asignaturas
    return asignaturas_dict

asignaturas_dict = generate_asignaturas(educacion)



def generate_unique_cod_asignaturas(asignaturas_dict):
    """
    Genera un diccionario con códigos únicos para cada asignatura.

    Args:
        asignaturas_dict (dict): Diccionario con asignaturas para cada titulación.

    Returns:
        dict: Diccionario con códigos únicos para cada asignatura.
    """
    cod_asignaturas = {}
    for titulacion, asignaturas in asignaturas_dict.items():
        for asignatura in asignaturas:
            cod_asignatura = asignatura[:4].upper() + fake.bothify(text='#####')
            cod_asignaturas[asignatura] = cod_asignatura
    return cod_asignaturas


cod_asignaturas_dict = generate_unique_cod_asignaturas(asignaturas_dict)
cod_plan_dict = {titulacion: fake.bothify(text='PLAN###??') for titulacion in asignaturas_dict.keys()}


def generate_alumnos(n):
    """
    Genera datos sintéticos para la tabla 'alumnos'.

    Args:
        n (int): Número de alumnos a generar.

    Returns:
        pd.DataFrame: DataFrame con los datos de los alumnos.
    """
    ids = [fake.unique.bothify(text='???#####') for _ in range(n)]
    anios_nac = np.random.randint(1980, 2000, n)
    universidades = random.choices(list(universidades_dict.keys()), k=n)
    cod_universidades = [universidades_dict[uni] for uni in universidades]
    abandona = random.choices(['si', 'no'], k=n)
    data = {
        'id': ids,
        'anio_nac': anios_nac,
        'universidad': universidades,
        'cod_universidad': cod_universidades,
        'abandona': abandona
    }
    return pd.DataFrame(data)


def generate_curso_aca(start_year, end_year):
    """
    Genera una lista de cursos académicos con el formato 'YYYY/YYYY+1'.

    Args:
        start_year (int): Año de inicio.
        end_year (int): Año de fin.
    
    Returns:
        list: Lista de cursos académicos.
    """
    return [f"{year}/{year+1}" for year in range(start_year, end_year)]

# Generar una lista de cursos académicos
cursos_academicos = generate_curso_aca(2017, 2024)


def generate_matricula(alumnos_df):
    """
    Genera datos sintéticos para la tabla 'matricula'.

    Args:
        alumnos_df (pd.DataFrame): DataFrame con los datos de los alumnos.
    
    Returns:
        pd.DataFrame: DataFrame con los datos de matrícula.
    """
    n = len(alumnos_df)
    num_matriculas = np.random.randint(1, 6, n)
    matricula_data = []
    for i, row in tqdm(alumnos_df.iterrows(), total=n, desc="matrícula"):
        titulacion = random.choice(list(asignaturas_dict.keys()))
        # Encontrar la rama correspondiente a la titulación
        rama = next(rama for rama, titulaciones in educacion.items() if titulacion in titulaciones)

        common_data = {
            'municipio': fake.city(),
            'nacionalidad': fake.country(),
            'provincia': fake.state(),
            'rama': rama,
            'sexo': random.choice(['Masculino', 'Femenino']),
            'titulacion': titulacion,
            'nombre_plan_propio': fake.word(),
            'universidad': row['universidad'],
            'cod_universidad': row['cod_universidad'],
            'cod_tipo_matricula': fake.bothify(text='T##'),
            'tipo_matricula': fake.word(),
            'cod_plan': cod_plan_dict[titulacion],
        }
        cursos_aca_usados = set()
        for j in range(num_matriculas[i]):
            curso_aca = random.choice([ca for ca in cursos_academicos if ca not in cursos_aca_usados])
            cursos_aca_usados.add(curso_aca)
            nuevo_ingreso = 'si' if j == 0 else 'no'
            matricula_data.append({
                'indice': len(matricula_data) + 1,
                'ambito_isced': fake.bothify(text='IS##'),
                'cod_plan': common_data['cod_plan'],
                'cod_mec': fake.bothify(text='MEC##'),
                'curso_aca': curso_aca,
                'municipio': common_data['municipio'],
                'nacionalidad': common_data['nacionalidad'],
                'nuevo_ingreso': nuevo_ingreso,
                'provincia': common_data['provincia'],
                'rama': common_data['rama'],
                'sexo': common_data['sexo'],
                'titulacion': common_data['titulacion'],
                'nombre_plan_propio': common_data['nombre_plan_propio'],
                'universidad': common_data['universidad'],
                'cod_universidad': common_data['cod_universidad'],
                'cod_tipo_matricula': common_data['cod_tipo_matricula'],
                'tipo_matricula': common_data['tipo_matricula'],
                'id': row['id']
            })
    return pd.DataFrame(matricula_data)


def generate_asignaturas_matriculadas(matricula_df, cod_asignaturas):
    """
    Genera datos sintéticos para la tabla 'asignaturas_matriculadas'.

    Args:
        matricula_df (pd.DataFrame): DataFrame con los datos de matrícula.
        cod_asignaturas (dict): Diccionario con códigos únicos para cada asignatura.

    Returns:
        pd.DataFrame: DataFrame con los datos de asignaturas matriculadas.
    """
    asignaturas_data = []
    for i, row in tqdm(matricula_df.iterrows(), total=len(matricula_df), desc="asignaturas_matriculadas"):
        num_asignaturas = min(random.randint(1, 20), len(asignaturas_dict[row['titulacion']]))
        asignaturas = random.sample(asignaturas_dict[row['titulacion']], num_asignaturas)
        for asignatura in asignaturas:
            cod_asignatura = cod_asignaturas[asignatura]
            asignaturas_data.append({
                'indice': len(asignaturas_data) + 1,
                'asignatura': asignatura,
                'cod_asignatura': cod_asignatura,
                'cod_plan': row['cod_plan'],
                'curso_aca': row['curso_aca'],
                'id': row['id'],
                'cod_tipologia': fake.bothify(text='T##'),
                'plan': row['titulacion'],
                'tipologia': fake.word(),
                'universidad': row['universidad'],
                'cod_universidad': row['cod_universidad']
            })
    return pd.DataFrame(asignaturas_data)


def generate_lineas_actas(asignaturas_matriculadas_df):
    """
    Genera datos sintéticos para la tabla 'lineas_actas'.

    Args:
        asignaturas_matriculadas_df (pd.DataFrame): DataFrame con los datos de asignaturas matriculadas.

    Returns:
        pd.DataFrame: DataFrame con los datos de actas.
    """
    actas_data = []
    for i, row in tqdm(asignaturas_matriculadas_df.iterrows(), total=len(asignaturas_matriculadas_df), desc="líneas_actas"):
        calif_numerica = round(random.uniform(0, 10), 2)
        if calif_numerica < 5:
            calif = 'Suspenso'
        elif calif_numerica < 7:
            calif = 'Aprobado'
        elif calif_numerica < 9:
            calif = 'Notable'
        else:
            calif = 'Sobresaliente'

        actas_data.append({
            'indice': len(actas_data) + 1,
            'asignatura': row['asignatura'],
            'calif_numerica': calif_numerica,
            'calif': calif,
            'cod_asig': row['cod_asignatura'],
            'cod_plan': row['cod_plan'],
            'conv': fake.bothify(text='C##'),
            'curso_aca': row['curso_aca'],
            'id': row['id'],
            'plan': row['plan'],
            'universidad': row['universidad'],
            'cod_universidad': row['cod_universidad']
        })
    return pd.DataFrame(actas_data)


def generate_docentes(n, universidades, cod_asignaturas, asignaturas_dict):
    """
    Genera datos sintéticos para la tabla 'docentes'.

    Args:
        n (int): Número de docentes a generar.
        universidades (dict): Diccionario con universidades y sus códigos.
        cod_asignaturas (dict): Diccionario con códigos únicos para cada asignatura.
        asignaturas_dict (dict): Diccionario con asignaturas para cada titulación.

    Returns:
        pd.DataFrame: DataFrame con los datos de los docentes.
    """
    docentes_data = []

    for i in tqdm(range(n), desc="docentes"):
        id_docente = fake.bothify(text='D#####')
        universidad, cod_universidad = random.choice(list(universidades.items()))

        num_asignaturas = random.randint(1, 5)
        asignaturas_seleccionadas = random.sample(list(cod_asignaturas.items()), num_asignaturas)

        for asignatura, cod_asignatura in asignaturas_seleccionadas:
            titulacion = next(titulacion for titulacion, asignaturas in asignaturas_dict.items() if asignatura in asignaturas)
            cod_plan = cod_plan_dict[titulacion]
            docentes_data.append({
                'indice': len(docentes_data) + 1,
                'id_docente': id_docente,
                'cod_universidad': cod_universidad,
                'universidad': universidad,
                'titulacion': titulacion,
                'cod_plan': cod_plan,
                'cod_asignatura': cod_asignatura,
                'asignatura': asignatura,
                'curso_aca': random.choice(cursos_academicos)
            })

    return pd.DataFrame(docentes_data)


def generate_ebau_prueba(n, alumnos_ids, universidades):
    """
    Genera datos sintéticos para la tabla 'ebau_prueba'.

    Args:
        n (int): Número de registros a generar.
        alumnos_ids (list): Lista de IDs de alumnos.
        universidades (dict): Diccionario con universidades y sus códigos.

    Returns:
        pd.DataFrame: DataFrame con los datos de las pruebas EBAU.
    """
    assert n == len(alumnos_ids), "El número de registros debe ser igual al número de alumnos"
    data = {
        'indice': range(1, n + 1),
        'conv': [fake.bothify(text='C##') for _ in range(n)],
        'curso_aca': np.random.choice(cursos_academicos, n),
        'especialidad': [fake.word() for _ in range(n)],
        'id': alumnos_ids,
        'nota_bach': np.round(np.random.uniform(5, 10, n), 2),
        'nota_def': np.round(np.random.uniform(5, 10, n), 2),
        'nota_prue': np.round(np.random.uniform(5, 10, n), 2),
        'universidad': np.random.choice(list(universidades.keys()), n),
    }
    data['cod_universidad'] = [universidades[uni] for uni in data['universidad']]

    return pd.DataFrame(data)


def generate_egresados(alumnos_df, matricula_df, lineas_actas_df):
    """
    Genera datos sintéticos para la tabla 'egresados'.
    
    Args:
        alumnos_df (pd.DataFrame): DataFrame con los datos de los alumnos.
        matricula_df (pd.DataFrame): DataFrame con los datos de matrícula.
        lineas_actas_df (pd.DataFrame): DataFrame con los datos de actas.
        
    Returns:
        pd.DataFrame: DataFrame con los datos de los egresados.
    """
    aprobados = lineas_actas_df[lineas_actas_df['calif_numerica'] >= 5].groupby('id').size()
    egresados_ids = aprobados[aprobados >= 38].index.tolist()
    alumnos_no_abandona = alumnos_df[alumnos_df['abandona'] == 'no']['id'].tolist()
    egresados_ids = [id for id in egresados_ids if id in alumnos_no_abandona]

    egresados_data = []
    for i, id_alumno in tqdm(enumerate(egresados_ids), total=len(egresados_ids), desc="egresados"):
        universidad, cod_universidad = alumnos_df.loc[alumnos_df['id'] == id_alumno, ['universidad', 'cod_universidad']].values[0]
        cod_plan = matricula_df.loc[matricula_df['id'] == id_alumno, 'cod_plan'].values[0]
        ultimo_curso_aca = matricula_df.loc[matricula_df['id'] == id_alumno, 'curso_aca'].max()
        egresados_data.append({
            'indice': i + 1,
            'cod_plan': cod_plan,
            'curso_aca': ultimo_curso_aca,
            'id': id_alumno,
            'nota_media': round(random.uniform(5, 10), 2),
            'plan': fake.word(),
            'universidad': universidad,
            'cod_universidad': cod_universidad
        })
    return pd.DataFrame(egresados_data)


def generate_gestores(n, universidades):
    """
    Genera datos sintéticos para la tabla 'gestores'.

    Args:
        n (int): Número de gestores a generar.
        universidades (dict): Diccionario con universidades y sus códigos.

    Returns:
        pd.DataFrame: DataFrame con los datos de los gestores.
    """
    data = {
        'gestor_id': range(1, n + 1),
        'universidad': np.random.choice(list(universidades.keys()), n)
    }
    data['cod_universidad'] = [universidades[uni] for uni in data['universidad']]
    return pd.DataFrame(data)


print("Generando datos....")
num_alumnos = 5
num_docentes = 1
num_gestores = 5

#Crea un directorio llamado src/data/csv si no existe

if not os.path.exists('src/data/csv'):
    os.makedirs('src/data/csv')

alumnos_df = generate_alumnos(num_alumnos)
matricula_df = generate_matricula(alumnos_df)
asignaturas_matriculadas_df = generate_asignaturas_matriculadas(matricula_df, cod_asignaturas_dict)
lineas_actas_df = generate_lineas_actas(asignaturas_matriculadas_df)
docentes_df = generate_docentes(num_docentes, universidades_dict, cod_asignaturas_dict, asignaturas_dict)
ebau_prueba_df = generate_ebau_prueba(num_alumnos, alumnos_df['id'].tolist(), universidades_dict)
egresados_df = generate_egresados(alumnos_df, matricula_df, lineas_actas_df)
gestores_df = generate_gestores(num_gestores, universidades_dict)

# Guarda datos en archivos CSV
alumnos_df.to_csv('src/data/csv/alumnos.csv', index=False)
matricula_df.to_csv('src/data/csv/matricula.csv', index=False)
asignaturas_matriculadas_df.to_csv('src/data/csv/asignaturas_matriculadas.csv', index=False)
lineas_actas_df.to_csv('src/data/csv/lineas_actas.csv', index=False)
docentes_df.to_csv('src/data/csv/docentes.csv', index=False)
ebau_prueba_df.to_csv('src/data/csv/ebau_prueba.csv', index=False)
egresados_df.to_csv('src/data/csv/egresados.csv', index=False)
gestores_df.to_csv('src/data/csv/gestores.csv', index=False)

print("Datos generados correctamente.")
