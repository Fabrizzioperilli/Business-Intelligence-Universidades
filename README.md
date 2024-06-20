# Business Intelligence para el sector académico (Universidades)

## Tabla de contenidos
1. [Descripción](#Descripción)
2. [Instalación](#Instalación)
3. [Uso](#Uso)
4. [Autor](#Autor)
5. [Licencia](#Licencia)


## Descripción
El presente proyecto representa el Trabajo de Fin de Grado (TFG) para el grado de Ingeniería Informática en la Universidad de La Laguna. 

El objetivo principal de este proyecto es la creación de un sistema de Business Intelligence (BI) para analizar y representar datos almacenados por las universidades. 

La herramienta dispone de cuadros de mandos con gráficos interactivos y un modelo de aprendizaje automático para predecir el abandono de los estudiantes en las universidades, permitiendo a los responsables de las universidades tomar decisiones basadas en datos y mejorar la calidad de la educación.

Con respecto al desarrollo de la herramienta, se ha utilizado el lenguaje de programación Python y la librería Dash para la creación de los cuadros de mando. Además, se ha utilizado la librería Scikit-learn para el desarrollo del modelo de aprendizaje automático.

## Instalación
Para utilizar la herramienta, es necesario tener instalado Python en su versión 3.6 o superior. Además, es necesario instalar un entorno virtual para instalar las dependencias del proyecto. Para ello, ejecute los siguientes comandos:

```bash
pip install virtualenv
```

Luego, cree un entorno virtual con el siguiente comando:

```bash
virtualenv venv
```

Active el entorno virtual con el siguiente comando:

```bash
source venv/bin/activate
```

Instale las dependencias del proyecto con el siguiente comando:

```bash
pip install -r requirements.txt
```
Es necesario tener instalado PostgreSQL en su sistema para poder utilizar la base de datos. Puede descargar PostgreSQL desde el siguiente enlace: https://www.postgresql.org/download/

Una vez instalado PostgreSQL, cree una base de datos con el nombre "dc_universities" y cargamos el backup de la base de datos con el siguiente comando:
  
  ```bash
  createdb db_universities
  ```

  ```bash
  psql -U postgres -d db_universities -f backup.sql
  ```

## Uso
Para levantar la aplicación, ejecute el siguiente comando:

```bash
python src/app.py
```

Esto levantará un servidor local en Flask en la dirección http://127.0.0.1:8050/. Abra su navegador y acceda a la dirección para visualizar la herramienta.


> [!NOTE]
> Se puede añadir más datos al sistema ejecutando el script `src/generate_synthetic_data.py`, este genera datos aleatorios en el direcotiro data/csv, una vez creado se pueden importar a la base de datos con el script `src/import_data.py` usando el sigueinte comando:

```bash
psql -U postgres -d db_universities -f import_data.sql
```
Luego se tiene que entrenar el modelo de aprendizaje con los nuevos datos, para ello se ejecuta el script `src/model.py` y se genera el modelo entrado en el directorio `model/`, luego ya se ejecutar la aplicación completa.


## Autor

Fabrizzio Daniell Perilli Martín 
alu0101138589@ull.edu.es

## Licencia









