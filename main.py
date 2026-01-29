import tkinter as tk
from tkinter import *


#Crear Ventana Principal
window = tk.Tk()
#Titulo
window.title("UI, Gestión FInanzas Personales")
#Dimensiones (Ancho x Altura)
window.geometry("600x550")
#Bloquear redimension
window.resizable(False, False)
#background
window.config(bg="darkgray")


#######MENU#######
#Crear barra de menu principal
menubar = tk.Menu(window)
window.config(menu=menubar)



#Crear submenu
file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Acción", menu=file_menu)

#Agregar comandos al submenu Accion
file_menu.add_command(label="Ingresos", command=None)
file_menu.add_command(label="Fondo de emergencia", command=None)
file_menu.add_command(label="Ahorro", command=None)
file_menu.add_command(label="Gastos de alimentación", command=None)
file_menu.add_command(label="Salud", command=None)
file_menu.add_separator()
file_menu.add_command(label="Salir", command=window.quit)



tk.mainloop()