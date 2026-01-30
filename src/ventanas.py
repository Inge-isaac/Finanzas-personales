import tkinter as tk


#Ventana Ingresos
def ventana_ingresos():
    root = tk.Tk()
    root.title("Ventana Ingresos")
    root.config(bg="darkgray")
    root.geometry("400x350")
    
    #Agregar un widget
    label = tk.Label(root, text="Gestion de ingresos", font="25", background="dimgray").pack(pady=20)
  
  
    #Obtiene el ancho y el alto de la pantalla del dispositivo
    ancho_pantalla = root.winfo_screenwidth()
    alto_pantalla = root.winfo_screenheight()

    #Establece el tamano de la ventana
    ancho_ventan = 400
    alto_ventan = 350

    #calcula la posicion X e Y pra centrar la ventana
    posicion_x = round(ancho_pantalla /2 - ancho_ventan /2)
    posicion_y = round(alto_pantalla /2 - alto_ventan /2)

    #Configura la geometria de la ventana
    root.geometry(f"{ancho_ventan}x{alto_ventan}+{posicion_x}+{posicion_y}")

    
    
#Ventana fondo de emergencia
def ventana_fondo_emergencias():
    root = tk.Tk()
    root.title("Fondo de emergencia")
    root.geometry("400x350")
    root.config(bg="darkgray")
    
    #Agregar widget
    label = tk.Label(root, text="Gestion fondo de emergencia", font="25", justify="center", background="dimgray").pack(pady=20)
    
    
    #Obtiene el ancho y el alto de la pantalla del dispositivo
    ancho_pantalla = root.winfo_screenwidth()
    alto_pantalla = root.winfo_screenheight()

    #Establece el tamano de la ventana
    ancho_ventan = 400
    alto_ventan = 350

    #calcula la posicion X e Y pra centrar la ventana
    posicion_x = round(ancho_pantalla /2 - ancho_ventan /2)
    posicion_y = round(alto_pantalla /2 - alto_ventan /2)

    #Configura la geometria de la ventana
    root.geometry(f"{ancho_ventan}x{alto_ventan}+{posicion_x}+{posicion_y}")
    
    root.mainloop()