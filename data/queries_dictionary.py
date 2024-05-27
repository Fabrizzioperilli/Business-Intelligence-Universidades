# Este diccionario contiene las consultas SQL utilizadas en el proyecto
queries = {
  "alumnado": {
      "common": {
          # Consulta para obtener los alumnos.
          "alumnos_all": """
                SELECT id FROM alumnos;
                """,
          # Consulta para obtener los datos que se muestran en el resumen de un alumno.
          "resumen_alumno": """
                SELECT DISTINCT universidad, titulacion, id 
                FROM matricula 
                WHERE id = :alumno_id AND titulacion = :titulacion;
                """,
          # Consulta para calcular la media de las calificaciones de un alumno en una titulación específica.
          "nota_media_alumno_titulacion": """
                SELECT AVG(li.calif_numerica) AS media_calif
                FROM public.lineas_actas li
                JOIN public.matricula m ON m.id = li.id AND m.cod_plan = li.cod_plan
                WHERE li.id = :alumno_id
                AND li.calif_numerica >= 5
                AND m.titulacion = :titulacion;
                """
      },
      "filters": {
          # Consulta para obtener los cursos académicos en los que un alumno está matriculado en una titulación específica.
          "curso_academico_alumnado": """
                SELECT curso_aca 
                FROM matricula 
                WHERE id = :alumno_id AND titulacion = :titulacion;
                """,
          # Consulta para obtener las asignaturas matriculadas por un alumno en un curso académico y titulación específicos.
          "asinaturas_matriculadas": """
                SELECT DISTINCT AM.asignatura 
                FROM asignaturas_matriculadas AM
                JOIN matricula MA ON AM.id = MA.id AND AM.cod_plan = MA.cod_plan
                WHERE AM.id = :alumno_id AND AM.curso_aca IN :curso_academico AND MA.titulacion = :titulacion;
                """,
          # Consulta para obtener las titulaciones de un alumno.
          "titulacion_alumnado": """
                SELECT DISTINCT titulacion 
                FROM matricula 
                WHERE id = :alumno_id;
                """
      },
      "graphs": {
          "personal": {
              # Consulta para obtener las asignaturas superadas por un alumno en un curso académico y titulación específicos.
              "curso_academico_asignaturas_superadas": """
                    SELECT li.curso_aca, COUNT(DISTINCT li.asignatura) AS N_asig_superada
                    FROM lineas_actas li
                    JOIN matricula ma ON li.id = ma.id AND li.cod_plan = ma.cod_plan
                    WHERE li.id = :alumno_id AND li.calif_numerica >= 5 AND li.curso_aca IN :curso_academico 
                    AND ma.titulacion = :titulacion
                    GROUP BY li.curso_aca
                    ORDER BY li.curso_aca;
                    """,
              # Consulta para obtener la calificación cualitativa más alta por curso académico y asignatura de un alumno.
              "calif_cualitativa_asginatura": """
                      WITH RankedGrades AS (
                        SELECT li.curso_aca, li.calif, 
                            ROW_NUMBER() OVER (PARTITION BY li.curso_aca, li.asignatura ORDER BY 
                                CASE 
                                    WHEN li.calif = 'Sobresaliente' THEN 5
                                    WHEN li.calif = 'Notable' THEN 4
                                    WHEN li.calif = 'Aprobado' THEN 3
                                    WHEN li.calif = 'Suspenso' THEN 2
                                    WHEN li.calif = 'No presentado' THEN 1
                                    ELSE 0 
                                END DESC) AS rk
                        FROM lineas_actas li
                        JOIN matricula ma ON li.id = ma.id AND li.cod_plan = ma.cod_plan
                        WHERE li.id = :alumno_id
                        AND li.curso_aca IN :curso_academico
                        AND ma.titulacion = :titulacion
                      )
                      SELECT curso_aca, calif, COUNT(*) AS grade_count
                      FROM RankedGrades
                      WHERE rk = 1
                      GROUP BY curso_aca, calif
                      ORDER BY curso_aca;
                      """,
                # Consulta para obtener la calificación numérica de las asignaturas matriculadas por un alumno.
                "calif_numerica_asignatura": """
                      SELECT li.asignatura, MAX(li.calif_numerica) AS calif_numerica
                      FROM lineas_actas li
                      JOIN matricula ma ON li.id = ma.id AND li.cod_plan = ma.cod_plan
                      WHERE li.id = :alumno_id 
                      AND li.curso_aca IN :curso_academico
                      AND ma.titulacion = :titulacion
                      GROUP BY li.asignatura
                      ORDER BY li.asignatura;
                      """,
                # Consulta para obtener el número de asignaturas matriculadas y superadas por un alumno.
                "asignaturas_matriculadas_y_superadas": """
                      SELECT 
                        AM.curso_aca AS "curso_academico",
                        COUNT(DISTINCT AM.asignatura) AS "Total asignaturas matriculadas",
                        COUNT(DISTINCT CASE WHEN LA.calif_numerica >= 5 THEN LA.asignatura ELSE NULL END) AS "Total asignaturas superadas"
                      FROM asignaturas_matriculadas AM
                      LEFT JOIN lineas_actas LA ON AM.cod_asignatura = LA.cod_asig AND AM.id = LA.id AND AM.curso_aca = LA.curso_aca
                      JOIN matricula MA ON AM.id = MA.id AND AM.cod_plan = MA.cod_plan
                      WHERE
                        AM.id = :alumno_id 
                        AND AM.curso_aca IN :curso_academico
                        AND MA.titulacion = :titulacion
                      GROUP BY
                        AM.curso_aca;
                      """
          },
          "general": {
                # Esta consulta devuelve el id de los alumnos, nota media, abandono y total de asignaturas superadas.
                "asignaturas_superadas_media_abandono": """
                      SELECT a.id, a.abandona, 
                      AVG(CASE WHEN la.max_calif >= 5 THEN la.max_calif ELSE NULL END) AS NotaMedia, 
                      COUNT(DISTINCT CASE WHEN la.max_calif >= 5 THEN la.asignatura ELSE NULL END) AS "Total asignaturas superadas"
                      FROM 
                          (
                            SELECT 
                                la.id, 
                                la.asignatura,
                                MAX(la.calif_numerica) AS max_calif
                            FROM  public.lineas_actas la
                            JOIN  public.matricula ma ON la.id = ma.id AND la.cod_plan = ma.cod_plan
                            WHERE 
                                la.curso_aca IN :curso_academico
                                AND la.asignatura IN :asignaturas_matriculadas
                                AND ma.titulacion = :titulacion
                            GROUP BY la.id, la.asignatura
                          ) la
                      JOIN public.alumnos a ON a.id = la.id 
                      GROUP BY a.id, a.abandona
                      ORDER BY a.id;
                """,
                # Consulta para obtener la calificación cualitativa de los alumnos para compararlo con los datos generales.
                "calif_cualitativa_comparativa": """
                      WITH CalificacionesMaximas AS (
                          SELECT
                              la.id,
                              la.asignatura,
                              la.curso_aca,
                              la.calif,
                              ROW_NUMBER() OVER (PARTITION BY la.id, la.curso_aca, la.asignatura ORDER BY CASE 
                                  WHEN la.calif = 'Sobresaliente' THEN 5
                                  WHEN la.calif = 'Notable' THEN 4
                                  WHEN la.calif = 'Aprobado' THEN 3
                                  WHEN la.calif = 'Suspenso' THEN 2
                                  WHEN la.calif = 'No presentado' THEN 1
                              ELSE 0 END DESC) AS rk
                              FROM lineas_actas la
                              JOIN 
                                  matricula ma ON la.id = ma.id AND la.cod_plan = ma.cod_plan
                              WHERE 
                                  la.curso_aca IN :curso_academico AND 
                                  la.asignatura IN :asignaturas_matriculadas AND 
                                  la.calif IN ('Sobresaliente', 'Notable', 'Aprobado', 'Suspenso', 'No presentado') AND
                                  ma.titulacion = :titulacion
                                )
                          SELECT
                              c.asignatura,
                              c.calif,
                              COUNT(*) AS count_grades
                          FROM CalificacionesMaximas c
                          WHERE c.rk = 1
                          GROUP BY c.asignatura, c.calif;
                          """,
                  # Consulta para obtener la calificación cualitativa del alumno.
                  "calif_cualitativa_alumno_asignaturas": """
                        WITH CalificacionesMaximas AS (
                              SELECT
                                  la.id,
                                  la.asignatura,
                                  la.curso_aca,
                                  la.calif,
                                  ROW_NUMBER() OVER (PARTITION BY la.id, la.curso_aca, la.asignatura ORDER BY CASE 
                                      WHEN la.calif = 'Sobresaliente' THEN 5
                                      WHEN la.calif = 'Notable' THEN 4
                                      WHEN la.calif = 'Aprobado' THEN 3
                                      WHEN la.calif = 'Suspenso' THEN 2
                                      WHEN la.calif = 'No presentado' THEN 1
                                      ELSE 0 END DESC) AS rk
                              FROM lineas_actas la
                              JOIN 
                                  matricula ma ON la.id = ma.id AND la.cod_plan = ma.cod_plan
                              WHERE 
                                  la.curso_aca IN :curso_academico AND 
                                  la.asignatura IN :asignaturas_matriculadas AND 
                                  la.id = :alumno_id AND 
                                  la.calif IN ('Sobresaliente', 'Notable', 'Aprobado', 'Suspenso', 'No presentado') AND
                                  ma.titulacion = :titulacion
                          )

                          SELECT
                              c.asignatura,
                              c.calif,
                              COUNT(*) AS count_grades
                          FROM 
                              CalificacionesMaximas c
                          WHERE 
                              c.rk = 1
                          GROUP BY 
                              c.asignatura, c.calif; 
                    """,
                    # Consulta para obtener la calificación media de los alumnos y la calificación del alumno.
                    "nota_media_general_mi_nota": """
                          SELECT 
                            subquery.asignatura, 
                            AVG(subquery.max_calif_numerica) AS media_calif,
                            MAX(CASE WHEN subquery.id = :alumno_id THEN subquery.max_calif_numerica ELSE NULL END) AS calif_alumno
                          FROM (
                            SELECT 
                                l.asignatura, 
                                l.id,
                                l.curso_aca,
                                MAX(l.calif_numerica) AS max_calif_numerica
                            FROM 
                                lineas_actas l
                            JOIN 
                                matricula m ON l.id = m.id AND l.cod_plan = m.cod_plan
                            WHERE 
                                l.asignatura IN :asignaturas_matriculadas AND 
                                l.curso_aca IN :curso_academico AND 
                                m.titulacion = :titulacion
                            GROUP BY 
                                l.asignatura, 
                                l.id,
                                l.curso_aca
                        ) subquery
                        GROUP BY 
                            subquery.asignatura
                        ORDER BY 
                            subquery.asignatura;
                         """
          }
      },
  },
  "docente": {
      "common": {
          # Consulta para obtener los docentes.
          "docentes_all": """
                SELECT DISTINCT id_docente FROM docentes;
                """,
          #Consulta para obtener los datos que se muestran en el resumen del docente 
          "resumen_docente": """
                SELECT DISTINCT universidad, titulacion, id_docente 
                FROM docentes 
                WHERE id_docente = :id_docente AND titulacion = :titulacion;
                """
      },
      "filters": {
          # Consulta para obtener las asignaturas de un docente según la titulación.
          "asignaturas_docente": """
                SELECT DISTINCT asignatura 
                FROM docentes 
                WHERE id_docente = :id_docente AND titulacion = :titulacion;
                """,
          # Consulta para obtener los cursos académicos de un docente según la asignatura.
          "curso_academico_docente": """
                SELECT curso_aca 
                FROM docentes 
                WHERE id_docente = :id_docente AND asignatura = :asignatura;
                """,
          # Consulta para obtener la titulación de un docente.
          "titulacion_docente": """
                SELECT DISTINCT titulacion 
                FROM docentes 
                WHERE id_docente = :id_docente;
                """,
          #Consulta para obtener todos los cursos acádemicos de las actas según la titulación
          "curso_academico_actas_titulacion": """
                SELECT DISTINCT li.curso_aca
                FROM lineas_actas li
                JOIN docentes ON li.cod_plan = docentes.cod_plan
                WHERE docentes.titulacion = :titulacion
                ORDER BY curso_aca;
                """,
          #Consulta para obtener todas las asignaturas por curso académico y titulación
          "asignaturas_actas_titulacion": """
                SELECT DISTINCT li.asignatura
                FROM lineas_actas li
                JOIN docentes ON li.cod_plan = docentes.cod_plan
                WHERE docentes.titulacion = :titulacion AND li.curso_aca = :curso_academico
                ORDER BY li.asignatura;

          """
      },
      "graphs": {
          "personal": {
              # Consulta para obtener el número de alumnos repetidores y de nuevo ingreso en una asignatura.
              "alumnos_repetidores_nuevos": """
                        WITH Asignatura AS (
                        SELECT DISTINCT am.id AS student_id, am.curso_aca
                        FROM public.asignaturas_matriculadas am
                        JOIN public.docentes d ON am.cod_asignatura = d.cod_asignatura
                        WHERE d.id_docente = :docente_id
                        AND am.asignatura = :asignaturas
                        AND am.curso_aca IN :curso_academico
                        ),
                        repetidores AS (
                            SELECT DISTINCT am.id AS student_id, MIN(am.curso_aca) AS primer_curso_aca
                            FROM public.asignaturas_matriculadas am
                            WHERE am.asignatura = :asignaturas
                            GROUP BY am.id
                            HAVING COUNT(am.curso_aca) > 1
                        ),
                        alumnos_categoria AS (
                            SELECT 
                                am.id,
                                am.curso_aca,
                                CASE 
                                    WHEN am.id IN (SELECT student_id FROM repetidores WHERE repetidores.primer_curso_aca <> am.curso_aca) THEN 'repetidor'
                                    ELSE 'nuevo_ingreso'
                                END AS categoria
                            FROM public.asignaturas_matriculadas am
                            WHERE am.asignatura = :asignaturas
                            AND am.curso_aca IN :curso_academico
                        )
                        SELECT
                            am.curso_aca AS curso_academico,
                            COUNT(DISTINCT am.id) FILTER (WHERE categoria = 'repetidor') AS alumnos_repetidores,
                            COUNT(DISTINCT am.id) FILTER (WHERE categoria = 'nuevo_ingreso') AS alumnos_nuevo_ingreso
                        FROM alumnos_categoria am
                        GROUP BY am.curso_aca
                        ORDER BY am.curso_aca;
                        """,
                  #Consulta para el número de alumnos por género en una asignatura.
                  "alumnos_genero_docente": """
                            WITH docente_asignaturas AS (
                            SELECT cod_asignatura
                            FROM public.docentes
                            WHERE id_docente = :id_docente
                              AND asignatura = :asignaturas
                            ),
                            asignaturas_matriculadas AS (
                                SELECT DISTINCT am.id, am.cod_asignatura, am.curso_aca
                                FROM public.asignaturas_matriculadas am
                                JOIN docente_asignaturas da ON am.cod_asignatura = da.cod_asignatura
                                WHERE am.curso_aca IN :curso_academico
                                  AND am.asignatura = :asignaturas
                            ),
                            estudiantes_sexo AS (
                                SELECT DISTINCT m.id AS alumno_id, m.sexo
                                FROM public.matricula m
                                JOIN asignaturas_matriculadas am ON m.id = am.id
                            )
                            SELECT am.curso_aca, m.sexo, COUNT(*) AS cantidad
                            FROM estudiantes_sexo m
                            JOIN asignaturas_matriculadas am ON m.alumno_id = am.id
                            GROUP BY am.curso_aca, m.sexo
                            ORDER BY am.curso_aca, m.sexo;
                    """,
                    #Consulta para obtener la nota media de los alumnos por asignatura y curso académico.
                    "alumnos_nota_media_docente": """
                            SELECT
                                l.curso_aca,  
                                l.asignatura, 
                                AVG(l.calif_numerica) AS media_calif
                            FROM 
                                lineas_actas l
                            WHERE 
                                l.asignatura IN :asignaturas AND 
                                l.curso_aca IN :curso_academico
                            GROUP BY 
                                l.curso_aca,
                                l.asignatura
                            ORDER BY 
                                l.curso_aca,
                                l.asignatura;
                                """,
                    #Consulta para obtener la nota cualitativa de los alumnos por asignatura y curso académico.
                      "alumnos_nota_cualitativa_docente": """
                            SELECT DISTINCT
                                l.curso_aca,  
                                l.calif, 
                                COUNT(*) AS num_alumnos
                            FROM 
                                lineas_actas l
                            WHERE 
                                l.asignatura = :asignaturas AND 
                                l.curso_aca IN :curso_academico
                            GROUP BY 
                                l.curso_aca,
                                l.calif
                            ORDER BY 
                                l.curso_aca,
                                l.calif;
                            """
          },
          "general": {
                  #Consulta para obtener el número de calificaciones cualitativas 
                  # de los alumnos por asignatura y curso académico.
                  "calif_all_cualitativa_asignaturas": """
                            SELECT DISTINCT li.curso_aca, 
                                  li.asignatura,  
                                  li.calif, 
                                  COUNT(DISTINCT li.id) AS n_alumnos
                            FROM lineas_actas li
                            JOIN docentes ON li.cod_plan = docentes.cod_plan
                            WHERE docentes.titulacion = :titulacion AND 
                                  li.curso_aca = :curso_academico AND 
                                  li.asignatura IN :asignaturas
                            GROUP BY li.curso_aca, li.asignatura, li.calif
                            ORDER BY li.asignatura;
                            """
          }
      },
  },
  "gestor": {
      "common": {
            #Consulta para obtener los gestores.
            "gestores_all": """
                SELECT DISTINCT gestor_id FROM gestores;
                """,
            #Consulta para obtener los datos que se muestran en el resumen del gestor.
            "resumen_gestor": """
                SELECT DISTINCT universidad, gestor_id
                FROM gestores
                WHERE gestor_id = :gestor_id;
                """,
            #Consulta para obtener el número de alumnos matriculados en una universidad.
            "numero_alumnos_matriculados_universidad": """
                SELECT COUNT(alumnos.id) AS n_alumnos_universidad
                FROM alumnos
                WHERE universidad = :universidad AND abandona = 'no';
                """,
            #Consulta que muestra la universidad de un gestor.
            "universidades_gestor": """
                SELECT DISTINCT cod_universidad
                FROM gestores 
                WHERE gestor_id = :gestor_id;
                """,
            "cursos_academicos_de_egresados": """
                SELECT DISTINCT curso_aca
                FROM egresados
                WHERE cod_universidad = :cod_universidad
            """
            
      },
      "filters": {
            #Consulta para obtener los cursos académicos de una universidad.
            "curso_academico_universidad": """
                SELECT DISTINCT curso_aca
                FROM matricula
                WHERE cod_universidad = :cod_universidad
                ORDER BY curso_aca;
                """,
            #Consulta para obtener las titulaciones de una universidad.
            "titulaciones_universidad_gestor": """
                SELECT DISTINCT titulacion
                FROM matricula
                WHERE cod_universidad = :cod_universidad AND curso_aca = :curso_academico;
                """
      },
      "graphs": {
          "indicadores": {
                #Consulta para obtener el número de alumnos de nuevo ingreso por género y titulación.
                "alumnos_nuevo_ingreso_genero_titulacion": """
                    SELECT curso_aca, titulacion, sexo, COUNT(*) as num_alumnos
                    FROM matricula
                    WHERE curso_aca = :curso_academico
                    AND titulacion IN :titulaciones
                    AND nuevo_ingreso = 'si'
                    AND cod_universidad = :cod_universidad
                    GROUP BY curso_aca, titulacion, sexo
                    ORDER BY titulacion;
                    """,
                #Consulta para obter el número de alumnos egresados por genero y titulación.
                "alumnos_egresados_genero_titulacion": """
                    SELECT 
                        m.titulacion AS Titulacion,
                        m.sexo AS Genero,
                        COUNT(DISTINCT m.id) AS Cantidad
                    FROM public.egresados e
                    JOIN public.matricula m ON e.cod_plan = m.cod_plan AND 
                            e.curso_aca = m.curso_aca AND e.id = m.id
                    WHERE e.cod_universidad = :cod_universidad AND 
                            m.curso_aca = :curso_academico AND 
                            m.titulacion IN :titulaciones
                    GROUP BY m.titulacion, m.sexo
                    ORDER BY m.titulacion, m.sexo;
                """,
                #Consulta para obtener el número de alumnos de nuevo ingreso por nacionalidad y titulación.
                "alumnos_nuevo_ingreso_nacionalidad_titulacion": """
                    SELECT titulacion, nacionalidad, COUNT(*) as num_alumnos
                    FROM matricula
                    WHERE curso_aca = :curso_academico
                    AND titulacion IN :titulaciones
                    AND nuevo_ingreso = 'si'
                    AND cod_universidad = :cod_universidad
                    GROUP BY titulacion, nacionalidad
                """,
                #Consulta para obtener el número de alumnos egresados por nacionalidad y titulación.
                "alumnos_egresados_nacionalidad_titulacion": """
                    SELECT 
                        m.titulacion AS Titulacion,
                        m.nacionalidad,
                        COUNT(DISTINCT m.id) AS Cantidad
                    FROM public.egresados e
                    JOIN public.matricula m ON e.cod_plan = m.cod_plan AND 
                         e.curso_aca = m.curso_aca AND e.id = m.id
                    WHERE e.cod_universidad = :cod_universidad AND 
                            m.curso_aca = :curso_academico AND 
                            m.titulacion IN :titulaciones
                    GROUP BY m.titulacion, m.nacionalidad
                    ORDER BY m.titulacion, m.nacionalidad;
                """
          },
          "resultados": {
                #Consulta para obtener la nota media de acceso de cada titulación.
                "nota_media_acceso_titulacion": """
                    SELECT ma.curso_aca, ma.titulacion,
                        AVG(eb.nota_prue) AS nota_ebau_media
                    FROM matricula ma
                    JOIN ebau_prueba eb ON ma.id = eb.id
                    WHERE nuevo_ingreso = 'si' AND ma.cod_universidad = :cod_universidad
                    GROUP BY ma.curso_aca, ma.titulacion
                    ORDER BY ma.curso_aca, ma.titulacion;
                """,
                #Consulta para obtener la duración media de los estudios con respecto a la nota media, por titulación y curso académico.
                "duracion_media_estudios_nota_gestor": """
                    WITH matriculas_por_estudiante AS (
                        SELECT
                            id,
                            titulacion,
                            COUNT(*) AS numero_matriculas
                        FROM matricula
                        GROUP BY id, titulacion
                    ),
                    media_notas_y_duracion AS (
                        SELECT
                            e.curso_aca,
                            m.titulacion,
                            m.rama,
                            AVG(e.nota_media) AS nota_media_curso_aca,
                            ROUND(AVG(mpe.numero_matriculas)) AS duracion_media_estudios
                        FROM egresados e
                        JOIN matricula m ON e.id = m.id AND e.cod_plan = m.cod_plan AND e.cod_universidad = m.cod_universidad
                        JOIN matriculas_por_estudiante mpe ON mpe.id = m.id AND mpe.titulacion = m.titulacion
                        WHERE e.cod_universidad = 'ULL015'
                        GROUP BY e.curso_aca, m.titulacion, m.rama
                    )
                    SELECT
                        nota_media_curso_aca,
                        titulacion,
                        rama,
                        curso_aca,
                        duracion_media_estudios
                    FROM media_notas_y_duracion
                    ORDER BY curso_aca;
                    """
          },
          "riesgo_abandono": {
                    #Consulta para obtener la tasa de abandono de una titulación.
                    "tasa_abandono_titulacion_gestor": """
                        WITH ultima_matricula AS (
                            SELECT 
                                m.id,
                                m.curso_aca,
                                m.titulacion,
                                t.abandona,
                                ROW_NUMBER() OVER (PARTITION BY m.id ORDER BY m.curso_aca DESC) AS row_num
                            FROM 
                                public.matricula m
                            JOIN 
                                public.alumnos t
                            ON 
                                m.id = t.id
                        )

                        SELECT 
                            m.curso_aca,
                            m.titulacion,
                            COUNT(DISTINCT m.id) AS numero_matriculados,
                            COUNT(DISTINCT CASE WHEN le.abandona = 'si' AND le.row_num = 1 THEN le.id END) AS numero_abandono
                        FROM 
                            public.matricula m
                        LEFT JOIN  ultima_matricula le ON m.id = le.id AND m.curso_aca = le.curso_aca
                        WHERE m.cod_universidad = :cod_universidad AND m.curso_aca IN :curso_academico
                        GROUP BY 
                            m.curso_aca,
                            m.titulacion
                        ORDER BY 
                            m.curso_aca,
                            m.titulacion;
                    """,
                    #Consulta para obtener la tasa de graduación de una titulación.
                    "tasa_graduacion_titulacion_gestor": """
                        SELECT 
                            COUNT(DISTINCT matricula.id) AS numero_matriculados,
                            COALESCE(COUNT( DISTINCT egresados.id), 0) AS numero_egresados,
                            matricula.curso_aca, 
                            matricula.titulacion
                        FROM 
                            matricula
                        LEFT JOIN 
                            egresados ON matricula.id = egresados.id
                        WHERE 
                            nuevo_ingreso = 'si' AND 
                            matricula.cod_universidad = :cod_universidad AND 
                            matricula.curso_aca IN :curso_academico
                        GROUP BY 
                            matricula.curso_aca, 
                            matricula.titulacion
                        ORDER BY 
                            titulacion, 
                            curso_aca;                    
                        """
          }
    },
  }
}