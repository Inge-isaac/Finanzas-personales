import tkinter as tk
from tkinter import ttk
import src.dimensiones as dm


def ventana_registro_usuario(master):
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
    nombre =ttk.Entry(root)
    nombre.grid(row=0, column=2, padx=5, pady=5)

    #Campo Genero
    tk.Label(
        root,
        text="Género:",
    ).grid(row=1, column=1, padx=5, pady=5, sticky = tk.E)
    gender_var = ttk.Combobox(root, 
                            values=["Masculino", "Femenino", "Otro"],
                            state ="readonly",
    )
    gender_var.grid(row=1, column=2, padx=5, pady=5, sticky=tk.W)


    #Campo de altura usuario
    tk.Label(
        root,
        text="Color de ojos (cm):",
    ).grid(row=2, column=1, padx=5, pady=5, sticky= tk.E)
    color_ojos = ttk.Combobox(
        root,
        values =["Negro", "Marrón", "Azul", "Verde", "Gris", "Otro"],
        state="readonly",
    )
    color_ojos.grid(row=2, column=2, padx=5, pady=5)


    #Campo peso usuario
    tk.Label(
        root,
        text="Peso (kg):",
    ).grid(row=3, column=1, padx=5, pady=5, sticky= tk.E)
    perso_corporarl = ttk.Entry(root)
    perso_corporarl.grid(row=3, column=2, padx=5, pady=5)

    #Boton registrar usuario
    btn_registrar = tk.Button(
        root,
        text="Registrar Usuario",
    )
    btn_registrar.grid(row=4, column=0, columnspan=3, pady=10)
    
    root.mainloop()
    
if __name__ == "__main__":
    ventana_registro_usuario()
    



