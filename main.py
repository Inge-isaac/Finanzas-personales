import tkinter as tk
#from tkinter import *
from src.ventanas import ventana_fondo_emergencias
from src.ventana_ingresos import ventana_registro_ingresos as vri
from src.dimensiones import center_window as cw



 
#Crear Ventana Principal
window = tk.Tk()
#Titulo
window.title("UI, Gestión FInanzas Personales")
#Bloquear redimension
window.resizable(False, False)
#Dimensiones
window.geometry("")
#background
window.config(bg="skyblue")
cw(window,600, 720) #Ejecuta el metodo del modulo dimensiones

#Widgets de la ventana principal


#######MENU#######
#Crear barra de menu principal
menubar = tk.Menu(window)
window.config(menu=menubar)

#Crear submenu
file_menu = tk.Menu(menubar, tearoff=0, bg="darkblue", fg="white") #fg(foreground, afecta el corlor de la fuente /texto)
menubar.add_cascade(label="Acción", menu=file_menu, foreground="white")

#Agregar comandos al submenu Accion
file_menu.add_command(label="Ingresos", command=lambda: vri(window))
file_menu.add_command(label="Fondo de emergencia", command=ventana_fondo_emergencias)
file_menu.add_command(label="Ahorro", command=None)
file_menu.add_command(label="Gastos de alimentación", command=None)
file_menu.add_command(label="Salud", command=None)
file_menu.add_separator()
file_menu.add_command(label="Salir", command=window.quit)


if __name__ == "__main__":
    tk.mainloop()

