import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import src.dimensiones as dm
import pyodbc
import data.conexion as cnx

#Conexion a la base de datos
cnx.get_db_connection()


#Funcion validacion
def validar_login():
    usuario = nombre_entry.get()
    password = pass_entry.get()

    if not usuario:
        tk.messagebox.showerror("Error", "Por favor, ingrese un nombre de usuario.")
        return
    
    try: 
        conn = cnx.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?,?)", (usuario, password))
        conn.commit()
        tk.messagebox.showinfo("Éxito", "Usuario registrado correctamente.")
    except Exception as e:
        tk.messagebox.showerror("Error", f"Error al registrar usuario: {e}")
         
        
        conn.close()
    except Exception as e:
        tk.messagebox.showerror("Error", f"Error al conectar a la base de datos: {e}")
            

def ventana_registro_usuario(master):
    #variable global
    global nombre_entry
    global pass_entry
    
    
    root = tk.Toplevel(master)
    root.title("Resgistro de usuario")
    root.resizable(False, False)
    root.config(bg="lightsteelblue")
    dm.center_window(root, 500,260)
    root.grab_set() # Hacer que la ventana sea modal

    #Imagen del perfil de usuario
    image = tk.PhotoImage(file="img/ing.png", master=root).subsample(5, 5)
    label_imagen = tk.Label(
        root,
        image=image,
        relief=tk.RAISED,
    )
    label_imagen.image = image # A veces Python elimina la imagen de la memoria antes de mostrarla. Para evitarlo, guarda la referencia en el objeto de la etiqueta
    label_imagen.grid(row=0, column=0, rowspan=4, padx=10 , pady=10)

    #Campo Nombre
    tk.Label(
        root,
        text="Nombre de usuario:",
    ).grid(row=0, column=1, padx=5, pady=5, sticky = tk.E)
    nombre_entry = ttk.Entry(root)
    nombre_entry.grid(row=0, column=2, padx=5, pady=5)

    #Campo password
    tk.Label(
        root,
        text="Password:",
    ).grid(row=1, column=1, padx=5, pady=5, sticky = tk.NE)
    pass_entry = ttk.Entry(root, show="*")
    pass_entry.grid(row=1, column=2, padx=5, pady=5, sticky=tk.NE)


    #Boton registrar usuario
    btn_registrar = tk.Button(
        root,
        text="Registrar Usuario",
        command=validar_login
    )
    btn_registrar.grid(row=4, column=0, columnspan=3, pady=10)
    
    root.mainloop()
    
if __name__ == "__main__":
    ventana_registro_usuario()
    



