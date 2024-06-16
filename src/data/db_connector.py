from sqlalchemy import create_engine, text
from sqlalchemy.pool import QueuePool
import json


class DatabaseConnector:
    """
    Clase para conectarse a la base de datos

    :param dbname: Nombre de la base de datos
    :param user: Usuario de la base de datos
    :param password: Contraseña del usuario
    :param host: Host de la base de datos
    :param port: Puerto de la base de datos
    :param pool_size: Tamaño del pool de conexiones
    :param max_overflow: Número máximo de conexiones que pueden ser creadas
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

        :param query: Consulta a ejecutar
        :param params: Parámetros de la consulta
        :return: Resultado de la consulta
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
