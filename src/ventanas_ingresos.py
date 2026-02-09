from logging import root
import os
import tkinter as tk
import pyodbc
from tkinter import messagebox, ttk as tkk
import src.utils.center_windows as cw
from data.conexion import get_db_connection
from src.utils.placeholder import PlaceholderEntry  as phe


"Configuracion de la conexion a la base de datos"
conn_str = get_db_connection()


#fUNCION PARA REGISTRAR INGRESOS
def registrar_ingreso():
    user = entry_user.get()
    categoria = entry_category.get()
    amount = entry_amount.get()
    fecha_incio = entry_fecha_inicio.get()
    fecha_fin = entry_fecha_fin.get()
    creado = entry_creado.get()
    
    
    
    if not user or not categoria or not amount or not fecha_incio or not fecha_fin or not creado:
        messagebox.showerror("Error", "Por favor, complete todos los campos.")
        return
    
    try:
        conn = pyodbc.connect(conn_str, timeout=5)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO budgets (user_id, category, amount, start_date, end_date, created_at) VALUES (?, ?, ?, ?, ?, ?)", (user, categoria, amount, fecha_incio, fecha_fin, creado))
        conn.commit()
        messagebox.showinfo("Éxito", "Ingreso registrado correctamente.")
        
        # Limpiar los campos después de registrar
        entry_user.delete(0, tk.END)
        entry_category.delete(0, tk.END)
        entry_amount.delete(0, tk.END)
        entry_fecha_inicio.delete(0, tk.END)
        entry_fecha_fin.delete(0, tk.END)
        entry_creado.delete(0, tk.END)
        
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
            cursor.execute("SELECT user_id, category, amount, start_date, end_date, created_at FROM budgets")
            filas = cursor.fetchall()
            
            for fila in filas:
                # Insertar al final de la tabla
                tabla.insert("", "end", values=(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5]))
              
        except Exception as e:
            print(f"Error al consultar: {e}")
        finally:
            conn.close()


def ventana_registro_ingresos(master):
    global entry_user, entry_amount, entry_fecha_inicio
    global entry_fecha_fin, entry_creado, entry_category
    global tabla
    
    
    #Interfaz grafica para registrar ingresos
    root = tk.Toplevel(master)
    root.title("Registrar Presupuesto")
    cw.center_window(root, 400, 500)
    root.config(bg="lightsteelblue")
    root.grab_set()  # Hacer que la ventana sea modal
    

    #Widgets
    # Configuración con GRID
    # El Label va en column=0 y el Entry en column=1
    tk.Label(root, bg="steelblue", fg="white", font=("Arial", 12), text="Id de usuario:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
    entry_user = tk.Entry(root)
    entry_user.grid(row=0, column=1, pady=5, sticky="w")
    
    tk.Label(root,bg="steelblue", fg="white", font=("Arial", 12), text="Categoría de presupuesto:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
    entry_category = tk.Entry(root)
    entry_category.grid(row=1, column=1, pady=5, sticky="w")

    tk.Label(root,bg="steelblue", fg="white", font=("Arial", 12), text="Registro de monto:").grid(row=2, column=0, sticky="e",columnspan=1, padx=5, pady=5)
    entry_amount = tk.Entry(root)
    entry_amount.grid(row=2, column=1, pady=5, sticky="w")

    tk.Label(root,bg="steelblue", fg="white", font=("Arial", 12), text="Fecha de inicio:").grid(row=3, column=0, sticky="e", padx=5, pady=5)
    entry_fecha_inicio = phe(root, placeholder="YYY-MM-DD")
    entry_fecha_inicio.grid(row=3, column=1, pady=5, sticky="w")
    
    tk.Label(root,bg="steelblue", fg="white", font=("Arial", 12), text="Fecha de finalización:").grid(row=4, column=0, sticky="e", padx=5, pady=5)
    entry_fecha_fin = tk.Entry(root)
    entry_fecha_fin.grid(row=4, column=1, pady=5, sticky="w")
    
    tk.Label(root,bg="steelblue", fg="white", font=("Arial", 12), text="Fecha de creación:").grid(row=5, column=0, sticky="e", padx=5, pady=5)
    entry_creado = tk.Entry(root)
    entry_creado.grid(row=5, column=1, pady=5, sticky="w")

    btn_registrar = tk.Button(root, text="Registrar Ingreso", command=registrar_ingreso)
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
        columns=("ID_usuario", "Categoria", "Monto", "Fecha Inicio", "Fecha Fin", "Fecha Creación"),
        show="headings",
        yscrollcommand=scroll_y.set,
        xscrollcommand=scroll_x.set
    )
    
    # Configurar columnas
    tabla.column("ID_usuario", anchor="w", width=50)     
    tabla.column("Categoria", anchor="center", width=70)   
    tabla.column("Monto", anchor="center", width=120)
    tabla.column("Fecha Inicio", anchor="center", width=100)
    tabla.column("Fecha Fin", anchor="center", width=100)
    tabla.column("Categoria", anchor="center", width=100)
    tabla.column("Fecha Creación", anchor="center", width=120)
    # Configurar encabezados
    tabla.heading("ID_usuario", text="ID Usuario", anchor="w")
    tabla.heading("Categoria", text="Categoría")
    tabla.heading("Monto", text="Monto")
    tabla.heading("Fecha Inicio", text="Fecha Inicio")
    tabla.heading("Fecha Fin", text="Fecha Fin")
    tabla.heading("Categoria", text="Categoría")
    tabla.heading("Fecha Creación", text="Fecha Creación")

    tabla.pack(fill="both", expand=True)

    # Conectar scrollbars
    scroll_y.config(command=tabla.yview)
    scroll_x.config(command=tabla.xview)

    
    root.mainloop()
    # Botón para activar la función

    #ventana_registro_ingresos()





















