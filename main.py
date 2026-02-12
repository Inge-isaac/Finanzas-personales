import tkinter as tk
#from tkinter import *
from src.ventanas_ingresos import ventana_registro_ingresos as vri
from src.ventana_transacciones import VentanaRegistrarTransaccion as vrt
from utils.center_windows import center_window as cw
from src.ventana_transacciones import VentanaRegistrarTransaccion

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
file_menu.add_separator()
file_menu.add_command(label="Salir", command=window.quit)



tk.mainloop()


