#
# @file db_connector.py
# @brief Este archivo contiene la clase DatabaseConnector para conectarse a la base de datos.
# @details Se define la clase DatabaseConnector con un método para ejecutar consultas en la base de datos.
# @version 1.0
# @date 04/05/2024
# @license MIT License
# @author Fabrizzio Daniell Perilli Martín
# @email alu0101138589@ull.edu.es
#

from sqlalchemy import create_engine, text
from sqlalchemy.pool import QueuePool
import json


class DatabaseConnector:
    """
    Clase para conectarse a la base de datos

    Attributes:
        db_url (str): URL de la base de datos
        engine (Engine): Motor de la base de datos

    Methods:
        execute_query: Ejecuta una consulta en la base de datos
        close: Cierra la conexión a la base de datos
    
    """
    def __init__(
        self, dbname, user, password, host, port, pool_size=5, max_overflow=10
    ):
        self.db_url = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}"
        self.engine = create_engine(
            self.db_url,
            poolclass=QueuePool,
            pool_size=pool_size,
            max_overflow=max_overflow,
        )

    def execute_query(self, query, params=None):
        """
        Ejecuta una consulta en la base de datos

        Args:
            query (str): Consulta SQL
            params (dict): Parámetros de la consulta

        Returns:
            list: Resultado de la consulta
        """
        with self.engine.connect() as connection:
            result = connection.execute(text(query), params or {})
            return result.fetchall()

    def close(self):
        """
        Cierra la conexión a la base de datos
        
        """
        self.engine.dispose()


with open("src/data/db_properties.json") as f:
    config = json.load(f)

# Se crea la instancia del conector
db = DatabaseConnector(
    dbname=config["dbname"],
    user=config["user"],
    password=config["password"],
    host=config["host"],
    port=config["port"],
)
