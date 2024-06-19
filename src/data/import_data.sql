-- Eliminar datos existentes de las tablas
DELETE FROM lineas_actas;
DELETE FROM egresados;
DELETE FROM alumnos;
DELETE FROM matricula;
DELETE FROM gestores;
DELETE FROM docentes;
DELETE FROM ebau_prueba;
DELETE FROM asignaturas_matriculadas;

-- Copiar datos desde los archivos CSV
\copy lineas_actas FROM 'csv/lineas_actas.csv' DELIMITER ',' CSV HEADER ENCODING 'UTF8';
\copy egresados FROM 'csv/egresados.csv' DELIMITER ',' CSV HEADER ENCODING 'UTF8';
\copy alumnos FROM 'csv/alumnos.csv' DELIMITER ',' CSV HEADER ENCODING 'UTF8';
\copy matricula FROM 'csv/matricula.csv' DELIMITER ',' CSV HEADER ENCODING 'UTF8';
\copy gestores FROM 'csv/gestores.csv' DELIMITER ',' CSV HEADER ENCODING 'UTF8';
\copy docentes FROM 'csv/docentes.csv' DELIMITER ',' CSV HEADER ENCODING 'UTF8';
\copy ebau_prueba FROM 'csv/ebau_prueba.csv' DELIMITER ',' CSV HEADER ENCODING 'UTF8';
\copy asignaturas_matriculadas FROM 'csv/asignaturas_matriculadas.csv' DELIMITER ',' CSV HEADER ENCODING 'UTF8';
