import tkinter as tk
from .dimensiones import center_window


#Ventana Ingresos
def ventana_ingresos():
    root = tk.Tk()
    root.title("Ventana Ingresos")
    root.config(bg="dimgray")
    center_window(root, 600, 500) #Uso dela funcion center_windows en el modulo  dimensiones
  
    
    #Agregar widget label instrucciones
    label_instrucciones = tk.Label(root, text="Ingrese la siguiente información:", font="15", background="dimgray", fg="white", justify="right")
    label_instrucciones.grid(row=0, column=0, columnspan=2, pady=5)
    #Agregar widget labels
    label1 = tk.Label(root, text="Fuente de ingreso:", font="5", background="dimgray", fg="black", justify="left")
    label1.grid(row=1, column=0, padx=5, pady=5)
    label2 = tk.Label(root, text="Monto del ingreso:", font="5", background="dimgray", fg="black", justify="left")
    label2.grid(row=2, column=0, padx=5, pady=5)
    label3 = tk.Label(root, text="Fecha del ingreso (DD/MM/AAAA):", font="5", background="dimgray", fg="black", justify="left")
    label3.grid(row=3, column=0, padx=5, pady=5)
    label4 = tk.Label(root, text="Categoría del ingreso:", font="5", background="dimgray", fg="black", justify="left")
    label4.grid(row=4, column=0, padx=5, pady=5)
    
    #Agregar widget entry
    entry1 = tk.Entry(root, width=30)
    entry1.grid(row=1, column=1, padx=2, pady=5, sticky="W")
    entry2 = tk.Entry(root, width=30)
    entry2.grid(row=2, column=1, padx=2, pady=5, sticky="W")
    entry3 = tk.Entry(root, width=30)
    entry3.grid(row=3, column=1, padx=2, pady=5, sticky="W")
    entry4 = tk.Entry(root, width=30)
    entry4.grid(row=4, column=1, padx=2, pady=5, sticky="W")
    root.grid_columnconfigure(1, weight=1) #centrar los entrys
    
    
    
    
    
#Ventana fondo de emergencia
def ventana_fondo_emergencias():
    root = tk.Tk()
    root.title("Fondo de emergencia")
    root.config(bg="dimgray")
    center_window(root, 400, 300) #Uso dela funcion center_windows en el modulo  dimensiones

    #Agregar widget
   # label = tk.Label(root, text="Gestion fondo de emergencia", font="25", justify="center", background="blue", fg="white").pack(pady=20)
    