import tkinter as tk

class Ventanadimensionada:
    #ventana
    w = tk.Tk()
    w.title("Ingreso")

    #Obtiene el ancho y el alto de la pantalla del dispositivo
    ancho_pantalla = w.winfo_screenwidth()
    alto_pantalla = w.winfo_screenheight()

    #Establece el tamano de la ventana
    ancho_ventan = 400
    alto_ventan = 350

    #calcula la posicion X e Y pra centrar la ventana
    posicion_x = round(ancho_pantalla /2 - ancho_ventan /2)
    posicion_y = round(alto_pantalla /2 - alto_ventan /2)

    #Configura la geometria de la ventana
    w.geometry(f"{ancho_ventan}x{alto_ventan}+{posicion_x}+{posicion_y}")


    w.mainloop()














