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
          },
          "general": {
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