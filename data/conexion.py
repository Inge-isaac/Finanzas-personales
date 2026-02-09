import pyodbc
import os

def get_db_connection():
     # Parámetros de conexión
    server = os.getenv("DB_SERVER", "localhost")
    database = os.getenv("DB_NAME", "personal_finances")
    user = os.getenv("DB_USER", "isaa")
    password = os.getenv("DB_PASSWORD", "123456")

    if not all([server, database, user, password]):
        raise ValueError("Faltan variables de entorno para la conexión a la BD")

    conn_str = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"UID={user};"
        f"PWD={password};"
        "TrustServerCertificate=yes;"
    )

    return conn_str

            
            
        
