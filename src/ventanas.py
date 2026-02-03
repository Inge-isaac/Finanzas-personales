import tkinter as tk
from .dimensiones import center_window



#Ventana fondo de emergencia
def ventana_fondo_emergencias():
    root = tk.Tk()
    root.title("Fondo de emergencia")
    root.config(bg="dimgray")
    center_window(root, 400, 300) #Uso dela funcion center_windows en el modulo  dimensiones

    #Agregar widget
   # label = tk.Label(root, text="Gestion fondo de emergencia", font="25", justify="center", background="blue", fg="white").pack(pady=20)
    