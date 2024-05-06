from sqlalchemy import create_engine, text
from sqlalchemy.pool import QueuePool
import json

class DatabaseConnector:
    def __init__(self, dbname, user, password, host, port, pool_size=5, max_overflow=10):
        self.db_url = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}"
        self.engine = create_engine(
            self.db_url,
            poolclass=QueuePool,
            pool_size=pool_size,
            max_overflow=max_overflow
        )

    def execute_query(self, query, params=None):
        with self.engine.connect() as connection:
            result = connection.execute(text(query), params or {})
            return result.fetchall()

    def execute_command(self, command, params=None):
        with self.engine.connect() as connection:
            connection.execute(text(command), params or {})

    def close(self):
        self.engine.dispose()
        
        
        
with open('data/db_properties.json') as f:
    config = json.load(f)

# Crear la instancia del conector
db = DatabaseConnector(
    dbname=config['dbname'],
    user=config['user'],
    password=config['password'],
    host=config['host'],
    port=config['port']
)

