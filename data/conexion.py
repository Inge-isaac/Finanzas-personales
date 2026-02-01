import pyodbc
import os
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO)

def get_db_connection():
    try:
        server = os.getenv("DB_SERVER")
        database = os.getenv("DB_NAME")
        user = os.getenv("DB_USER")
        password = os.getenv("DB_PASS")

        # Validar variables de entorno
        if not all([server, database, user, password]):
            raise ValueError("Faltan variables de entorno para la conexión a la BD")

        conn = pyodbc.connect(
            f"DRIVER={{ODBC Driver 17 for SQL Server}};"
            f"SERVER={server};"
            f"DATABASE={database};"
            f"UID={user};"
            f"PWD={password};"
            "Encrypt=yes;"
            "TrustServerCertificate=yes;"
            "Connection Timeout=5;"
        )

        logging.info("Conexión a SQL Server establecida correctamente")
        return conn

    except pyodbc.Error as e:
        logging.error(f"Error de SQL Server: {e}")
        return None

    except Exception as e:
        logging.error(f"Error general: {e}")
        return None
