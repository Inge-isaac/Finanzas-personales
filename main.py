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

#Ventana Ingresos
def ventana_ingresos():
    ventana_ingresos = tk.Toplevel(window)#Crear ventana secundaria (Toplevel)
    ventana_ingresos.title("Ingeresos")
    ventana_ingresos.geometry("400x350")
    ventana_ingresos.config(bg="darkgray")
    
    #Agregar un widget
    label = tk.Label(ventana_ingresos, text="Gestion de ingresos", font="25", background="green")
    label.pack(pady=20)
    
#Ventana fondo de emergencia
def ventana_fondo_emergencias():
    ventana_fe = tk.Toplevel(window)
    ventana_fe.title("Fondo de emergencia")
    ventana_fe.geometry("400x350")
    ventana_fe.config(bg="darkgray")
    
    #Agregar widget
    label = tk.Label(ventana_fe, text="Gestion fondo de emergencia", font="25", background="green")
    label.pack(pady=20)
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