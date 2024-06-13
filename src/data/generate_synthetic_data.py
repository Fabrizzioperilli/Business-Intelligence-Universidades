import pandas as pd
import numpy as np
from faker import Faker
import random

# Inicialización de Faker
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
        ],
        'Enfermería': [
            'Cuidados Básicos', 'Enfermería Quirúrgica', 'Enfermería Pediátrica', 'Enfermería Geriátrica', 'Salud Pública',
            'Salud Mental', 'Enfermería Obstétrica', 'Cuidados Críticos', 'Fundamentos de Enfermería', 'Enfermería Comunitaria',
            'Enfermería Familiar', 'Farmacología para Enfermería', 'Anatomía y Fisiología', 'Ética y Deontología',
            'Terapias Alternativas', 'Gestión en Enfermería', 'Educación para la Salud', 'Metodología de la Investigación',
            'Enfermería Oncológica', 'Enfermería de Urgencias', 'Nutrición y Dietética', 'Cuidados Paliativos'
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
        ],
        'Contabilidad': [
            'Contabilidad Financiera', 'Contabilidad de Costos', 'Auditoría', 'Contabilidad Gerencial', 'Fiscalidad',
            'Normas Internacionales de Contabilidad', 'Contabilidad de Sociedades', 'Análisis Financiero', 'Contabilidad Pública',
            'Sistemas de Información Contable', 'Contabilidad Forense', 'Contabilidad Ambiental', 'Contabilidad de Gestión',
            'Ética Profesional', 'Contabilidad Internacional', 'Contabilidad Presupuestaria', 'Planificación Financiera',
            'Tributación', 'Control Interno', 'Tecnología en Contabilidad', 'Regulación Contable', 'Evaluación de Riesgos',
            'Contabilidad de Activos', 'Contabilidad de Pasivos', 'Revisión Contable'
        ],
        'Finanzas': [
            'Finanzas Corporativas', 'Mercados Financieros', 'Gestión de Inversiones', 'Finanzas Internacionales', 'Análisis de Riesgos',
            'Planificación Financiera', 'Economía Financiera', 'Ingeniería Financiera', 'Finanzas Personales', 'Gestión de Portafolios',
            'Valoración de Empresas', 'Banca y Seguros', 'Derivados Financieros', 'Matemáticas Financieras', 'Ética Financiera',
            'Finanzas Públicas', 'Gestión del Riesgo Financiero', 'Fintech', 'Modelos Financieros', 'Toma de Decisiones Financieras',
            'Gestión de Tesorería', 'Política Monetaria', 'Evaluación de Proyectos', 'Regulación Financiera', 'Innovación Financiera'
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

# Generar asignaturas para cada titulación
def generate_asignaturas(educacion, min_asignaturas=38):
    asignaturas_dict = {}
    for rama, titulaciones in educacion.items():
        for titulacion, palabras in titulaciones.items():
            num_asignaturas = min(min_asignaturas, len(palabras))
            asignaturas = random.sample(palabras, num_asignaturas)
            asignaturas_dict[titulacion] = asignaturas
    return asignaturas_dict

# Generar diccionario de asignaturas
asignaturas_dict = generate_asignaturas(educacion)

# Función para generar códigos únicos de asignaturas
def generate_unique_cod_asignaturas(asignaturas_dict):
    cod_asignaturas = {}
    for titulacion, asignaturas in asignaturas_dict.items():
        for asignatura in asignaturas:
            cod_asignatura = asignatura[:4].upper() + fake.bothify(text='#####')
            cod_asignaturas[asignatura] = cod_asignatura
    return cod_asignaturas

# Generar un diccionario con códigos únicos para cada asignatura
cod_asignaturas_dict = generate_unique_cod_asignaturas(asignaturas_dict)

# Función para generar datos sintéticos para la tabla 'alumnos'
def generate_alumnos(n):
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

# Función para generar cursos académicos en formato "YYYY/YYYY"
def generate_curso_aca(start_year, end_year):
    return [f"{year}/{year+1}" for year in range(start_year, end_year)]

# Generar una lista de cursos académicos
cursos_academicos = generate_curso_aca(2017, 2024)

# Función para generar datos sintéticos para la tabla 'matricula'
def generate_matricula(alumnos_df):
    n = len(alumnos_df)
    num_matriculas = np.random.randint(1, 6, n)
    matricula_data = []
    for i, row in alumnos_df.iterrows():
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
            'cod_plan': fake.bothify(text='PLAN##'),
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

# Función para generar datos sintéticos para la tabla 'asignaturas_matriculadas'
def generate_asignaturas_matriculadas(matricula_df, cod_asignaturas):
    asignaturas_data = []
    for i, row in matricula_df.iterrows():
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

# Función para generar datos sintéticos para la tabla 'lineas_actas'
def generate_lineas_actas(asignaturas_matriculadas_df):
    actas_data = []
    for i, row in asignaturas_matriculadas_df.iterrows():
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

# Función para generar datos sintéticos para la tabla 'docentes'
def generate_docentes(n, universidades, cod_asignaturas):
    docentes_data = []
    
    for i in range(n):
        id_docente = fake.bothify(text='D#####')
        universidad, cod_universidad = random.choice(list(universidades.items()))
        
        num_asignaturas = random.randint(1, 5)
        asignaturas_seleccionadas = random.sample(list(cod_asignaturas.items()), num_asignaturas)
        
        for asignatura, cod_asignatura in asignaturas_seleccionadas:
            docentes_data.append({
                'indice': len(docentes_data) + 1,
                'id_docente': id_docente,
                'cod_universidad': cod_universidad,
                'universidad': universidad,
                'titulacion': random.choice(list(asignaturas_dict.keys())),
                'cod_plan': fake.bothify(text='PLAN##'),
                'cod_asignatura': cod_asignatura,
                'asignatura': asignatura,
                'curso_aca': random.choice(cursos_academicos)
            })
    
    return pd.DataFrame(docentes_data)

# Función para generar datos sintéticos para la tabla 'ebau_prueba'
def generate_ebau_prueba(n, alumnos_ids, universidades):
    assert n == len(alumnos_ids), "El número de registros debe ser igual al número de alumnos"

    # Generar datos para cada campo
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

# Función para generar datos sintéticos para la tabla 'egresados'
def generate_egresados(alumnos_df, matricula_df, lineas_actas_df):
    aprobados = lineas_actas_df[lineas_actas_df['calif_numerica'] >= 5].groupby('id').size()
    egresados_ids = aprobados[aprobados >= 38].index.tolist()
    alumnos_no_abandona = alumnos_df[alumnos_df['abandona'] == 'no']['id'].tolist()
    egresados_ids = [id for id in egresados_ids if id in alumnos_no_abandona]

    egresados_data = []
    for i, id_alumno in enumerate(egresados_ids):
        universidad, cod_universidad = alumnos_df.loc[alumnos_df['id'] == id_alumno, ['universidad', 'cod_universidad']].values[0]
        cod_plan = matricula_df.loc[matricula_df['id'] == id_alumno, 'cod_plan'].values[0]
        ultimo_curso_aca = matricula_df.loc[matricula_df['id'] == id_alumno, 'curso_aca'].max()
        egresados_data.append({
            'indice': i + 1,
            'cod_plan': cod_plan,
            'curso_aca': ultimo_curso_aca,
            'id': id_alumno,
            'nota_media': round(random.uniform(5, 10), 2),
            'plan': random.choice(list(asignaturas_dict.keys())),
            'universidad': universidad,
            'cod_universidad': cod_universidad
        })
    return pd.DataFrame(egresados_data)

# Función para generar datos sintéticos para la tabla 'gestores'
def generate_gestores(n, universidades):
    data = {
        'gestor_id': range(1, n + 1),
        'universidad': np.random.choice(list(universidades.keys()), n)
    }
    data['cod_universidad'] = [universidades[uni] for uni in data['universidad']]
    return pd.DataFrame(data)


num_alumnos = 150000
num_docentes = 2000
num_gestores = 50

alumnos_df = generate_alumnos(num_alumnos)
matricula_df = generate_matricula(alumnos_df)
asignaturas_matriculadas_df = generate_asignaturas_matriculadas(matricula_df, cod_asignaturas_dict)
lineas_actas_df = generate_lineas_actas(asignaturas_matriculadas_df)
docentes_df = generate_docentes(num_docentes, universidades_dict, cod_asignaturas_dict)
ebau_prueba_df = generate_ebau_prueba(num_alumnos, alumnos_df['id'].tolist(), universidades_dict)
egresados_df = generate_egresados(alumnos_df, matricula_df, lineas_actas_df)
gestores_df = generate_gestores(num_gestores, universidades_dict)

# Guardar datos en archivos CSV
alumnos_df.to_csv('alumnos.csv', index=False)
matricula_df.to_csv('matricula.csv', index=False)
asignaturas_matriculadas_df.to_csv('asignaturas_matriculadas.csv', index=False)
lineas_actas_df.to_csv('lineas_actas.csv', index=False)
docentes_df.to_csv('docentes.csv', index=False)
ebau_prueba_df.to_csv('ebau_prueba.csv', index=False)
egresados_df.to_csv('egresados.csv', index=False)
gestores_df.to_csv('gestores.csv', index=False)
