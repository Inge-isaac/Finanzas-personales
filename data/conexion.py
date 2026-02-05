import pyodbc


def get_db_connection():
     # Parámetros de conexión
    conn_str = (
        "Driver={ODBC Driver 17 for SQL Server};"
        "Server=EL-ZURDO;"
        "Database=personal_finances;"
        "UID=isaa;"
        "PWD=123456;"
    )
   
    try:
        connection = pyodbc.connect(conn_str)
        print("Conexión exitosa a la base de datos.")
        return connection
    except pyodbc.Error as e:
        print("Error al conectar a la base de datos:", e)
        return None

get_db_connection()

            
            
        
