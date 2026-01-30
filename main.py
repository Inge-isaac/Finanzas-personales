import tkinter as tk
from tkinter import *
from src.ventanas import ventana_ingresos, ventana_fondo_emergencias

    
#Crear Ventana Principal
window = tk.Tk()
#Titulo
window.title("UI, Gestión FInanzas Personales")
#Bloquear redimension
window.resizable(False, False)
#background
window.config(bg="darkgray")



#Obtiene el ancho y el alto de la pantalla del dispositivo
ancho_pantalla = window.winfo_screenwidth()
alto_pantalla = window.winfo_screenheight()

#Establece el tamano de la ventana
ancho_ventan = 500
alto_ventan = 450

#calcula la posicion X e Y pra centrar la ventana
posicion_x = round(ancho_pantalla /2 - ancho_ventan /2)
posicion_y = round(alto_pantalla /2 - alto_ventan /2)

#Configura la geometria de la ventana
window.geometry(f"{ancho_ventan}x{alto_ventan}+{posicion_x}+{posicion_y}")




#######MENU#######
#Crear barra de menu principal
menubar = tk.Menu(window)
window.config(menu=menubar)

#Crear submenu
file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Acción", menu=file_menu)

#Agregar comandos al submenu Accion
file_menu.add_command(label="Ingresos", command=ventana_ingresos)
file_menu.add_command(label="Fondo de emergencia", command=ventana_fondo_emergencias)
file_menu.add_command(label="Ahorro", command=None)
file_menu.add_command(label="Gastos de alimentación", command=None)
file_menu.add_command(label="Salud", command=None)
file_menu.add_separator()
file_menu.add_command(label="Salir", command=window.quit)



tk.mainloop()
