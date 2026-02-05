import os
import tkinter as tk
import pyodbc
from tkinter import messagebox, ttk as tkk
import src.dimensiones as dm


"Configuracion de la conexion a la base de datos"

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


#fUNCION PARA REGISTRAR INGRESOS
def registrar_ingreso():
    acount = entry_account.get()
    amount = entry_amount.get()
    transaction = entry_transaction.get()
    description = entry_description.get()
    category = entry_category.get()
    created = entry_created.get()
    
    
    if not acount or not amount or not category or not created or not transaction or not description:
        messagebox.showerror("Error", "Por favor, complete todos los campos.")
        return
    
    try:
        conn = pyodbc.connect(conn_str, timeout=5)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO transactions (account_id, amount, transaction_date, description, category, created_at) VALUES (?, ?, ?, ?, ?, ?)", (acount, amount, transaction, description, category, created))
        conn.commit()
        messagebox.showinfo("Éxito", "Ingreso registrado correctamente.")
        
        # Limpiar los campos después de registrar
        entry_account.delete(0, tk.END)
        entry_amount.delete(0, tk.END)
        entry_transaction.delete(0, tk.END)
        entry_description.delete(0, tk.END)
        entry_category.delete(0, tk.END)
        entry_created.delete(0, tk.END)
        
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo registrar el ingreso: {e}")
    
    finally:
        if 'conn' in locals() and conn:
            conn.close()
            

def mostrar_registros():
    # Limpiar tabla para evitar duplicados al refrescar
    for fila in tabla.get_children():
        tabla.delete(fila)
        
#Funcion mostrar registros desde la base de datos
    conn = pyodbc.connect(conn_str, timeout=5)
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT account_id, amount, transaction_date, description, category, created_at FROM transactions")
            filas = cursor.fetchall()
            
            for fila in filas:
                # Insertar al final de la tabla
                tabla.insert("", "end", values=(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5]))
                if fila[1] < 0:
                    tabla.item(tabla.get_children()[-1], tags=("negativo",))
                    tabla.tag_configure("negativo", foreground="orangered", font=("Arial", 8, "bold"))
                elif fila[1] > 0:
                    tabla.item(tabla.get_children()[-1], tags=("positivo",))
                    tabla.tag_configure("positivo", foreground="limegreen", font=("Arial", 8, "bold"))
            
              
        except Exception as e:
            print(f"Error al consultar: {e}")
        finally:
            conn.close()


def ventana_registrar_transaccion(master):
    global entry_account, entry_amount, entry_transaction
    global entry_description, entry_category, entry_created
    global tabla

    
    
    #Interfaz grafica para registrar ingresos
    root = tk.Toplevel(master)
    root.title("Registrar Transaccion")
    dm.center_window(root, 400, 500)
    root.config(bg="lightsteelblue")
    root.grab_set()  # Hacer que la ventana sea modal
    

    #Widgets
    # Configuración con GRID
    # El Label va en column=0 y el Entry en column=1
    tk.Label(root, bg="steelblue", fg="white", font=("Arial", 12), text="Id de la Cuenta:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
    entry_account = tk.Entry(root)
    entry_account.grid(row=0, column=1, pady=5, sticky="w")

    tk.Label(root,bg="steelblue", fg="white", font=("Arial", 12), text="Registro de monto:").grid(row=1, column=0, sticky="e",columnspan=1, padx=5, pady=5)
    entry_amount = tk.Entry(root)
    entry_amount.grid(row=1, column=1, pady=5, sticky="w")
    tk.Label(root,bg="steelblue", fg="white", font=("Arial", 12), text="Fecha de transacción:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
    entry_transaction = tk.Entry(root)
    entry_transaction.grid(row=2, column=1, pady=5, sticky="w")

    tk.Label(root,bg="steelblue", fg="white", font=("Arial", 12), text="Descripción de transacción:").grid(row=3, column=0, sticky="e", padx=5, pady=5)
    entry_description = tk.Entry(root)
    entry_description.grid(row=3, column=1, pady=5, sticky="w")

    tk.Label(root,bg="steelblue", fg="white", font=("Arial", 12), text="Categoría de transacción:").grid(row=4, column=0, sticky="e", padx=5, pady=5)
    entry_category = tk.Entry(root)
    entry_category.grid(row=4, column=1, pady=5, sticky="w")

    tk.Label(root,bg="steelblue", fg="white", font=("Arial", 12), text="Fecha (YYYY-MM-DD):").grid(row=5, column=0, sticky="e", padx=5, pady=5)
    entry_created = tk.Entry(root)
    entry_created.grid(row=5, column=1, pady=5, sticky="w")

    btn_registrar = tk.Button(root, text="Registrar Transacción", command=ventana_registrar_transaccion)
    btn_registrar.grid(row=6, column=0, columnspan=2, pady=20)


    btn_consultar = tk.Button(root, text="Actualizar Lista", command=mostrar_registros)
    btn_consultar.grid(row=7, column=0, columnspan=2, pady=10)
    
    # ===== FRAME PARA LA TABLA =====
    frame_tabla = tk.Frame(root)
    frame_tabla.grid(row=8, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)

    # Permitir expansión
    root.grid_rowconfigure(8, weight=1)
    root.grid_columnconfigure(1, weight=1)

    # Scrollbar vertical
    scroll_y = tk.Scrollbar(frame_tabla, orient="vertical")
    scroll_y.pack(side="right", fill="y")

    # Scrollbar horizontal (opcional)
    scroll_x = tk.Scrollbar(frame_tabla, orient="horizontal")
    scroll_x.pack(side="bottom", fill="x")

    # Treeview
    tabla = tkk.Treeview(
        frame_tabla,
        columns=("ID_Acount", "Monto", "Fecha Transacción", "Descripción", "Categoría", "Fecha Creación"),
        show="headings",
        yscrollcommand=scroll_y.set,
        xscrollcommand=scroll_x.set
    )
    
    # Configurar columnas
    tabla.column("ID_Acount", anchor="w", width=50)     
    tabla.column("Monto", anchor="center", width=70)   
    tabla.column("Fecha Transacción", anchor="center", width=120)
    tabla.column("Descripción", anchor="w", width=100)
    tabla.column("Categoría", anchor="center", width=100)
    tabla.column("Fecha Creación", anchor="center", width=120)
    # Configurar encabezados
    tabla.heading("ID_Acount", text="ID Cuenta", anchor="w")
    tabla.heading("Monto", text="Monto")
    tabla.heading("Fecha Transacción", text="Fecha Transacción")
    tabla.heading("Descripción", text="Descripción")
    tabla.heading("Categoría", text="Categoría")
    tabla.heading("Fecha Creación", text="Fecha Creación")

    tabla.pack(fill="both", expand=True)

    # Conectar scrollbars
    scroll_y.config(command=tabla.yview)
    scroll_x.config(command=tabla.xview)

    
    #root.mainloop()
    # Botón para activar la función

    #ventana_registro_ingresos()





















