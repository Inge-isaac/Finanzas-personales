
#Este módulo solo se encarga de calcular y aplicar la posición de la ventana, nada más.
def center_window(w, ancho, alto):

    #Obtiene el ancho y el alto de la pantalla del dispositivo
    ancho_pantalla = w.winfo_screenwidth()
    alto_pantalla = w.winfo_screenheight()


    #calcula la posicion X e Y pra centrar la ventana
    posicion_x = round(ancho_pantalla  - ancho) //2
    posicion_y = round(alto_pantalla - alto) //2

    #Configura la geometria(posición), de la ventana
    w.geometry(f"{ancho}x{alto}+{posicion_x}+{posicion_y}")

    















