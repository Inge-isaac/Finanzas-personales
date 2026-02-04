import tkinter as tk
#from tkinter import *
from src.ventanas_ingresos import ventana_registro_ingresos as vri
from src.ventana_transacciones import ventana_registrar_transaccion as vrt
from src.dimensiones import center_window as cw
from src.ventana_login import ventana_registro_usuario as vru


 
#Crear Ventana Principal
window = tk.Tk()
#Titulo
window.title("UI, Gestión FInanzas Personales")
#Bloquear redimension
window.resizable(False, False)
#Dimensiones
window.geometry("")
#background
window.config(bg="steelblue")
cw(window,600, 550) #Ejecuta el metodo del modulo dimensiones

#Widgets de la ventana principal


#######MENU#######
#Crear barra de menu principal
menubar = tk.Menu(window)
window.config(menu=menubar)

#Crear submenu
file_menu = tk.Menu(menubar, tearoff=0, bg="darkblue", fg="white") #fg(foreground, afecta el corlor de la fuente /texto)
menubar.add_cascade(label="Acción", menu=file_menu, foreground="white")

#Agregar comandos al submenu Accion
file_menu.add_command(label="Presupuestos", command=lambda: vri(window))
file_menu.add_command(label="Transacciones", command=lambda: vrt(window))
file_menu.add_command(label="Registro usuario", command=lambda: vru(window))
file_menu.add_command(label="Gastos de alimentación", command=None)
file_menu.add_command(label="Salud", command=None)
file_menu.add_separator()
file_menu.add_command(label="Salir", command=window.quit)


tk.mainloop()

