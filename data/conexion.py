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
        #Establecer la conexion
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        print("Conexión exitosa a la base de datos.")
        
        #Ejecutar consulta
        cursor.execute("SELECT * FROM accounts;")
        for row  in cursor.fetchall():
            print(row)
    except Exception as e:
        print(f"Error: {e}")
        
    finally: 
        #Cerrar conexion 
        if 'connn' in locals() and conn:
            conn.close()
            print("Conexion cerrada.")
        
get_db_connection()
            
            
        
