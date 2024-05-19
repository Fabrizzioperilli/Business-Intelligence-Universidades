# Este diccionario contiene las consultas SQL utilizadas en el proyecto
queries = {
  "alumnado": {
      "common": {
          # Consulta para obtener los alumnos.
          "alumnos": """
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
      },
      "filters": {
      },
      "graphs": {
          "personal": {
          },
          "general": {
          }
      },
  },
  "gestor": {
      "common": {
      },
      "filters": {
      },
      "graphs": {
          "personal": {
          },
          "general": {
          }
      },
  }
}