from tkinter import *

# Inicializar ventana
ventana = Tk()

# Propiedades de ventana
ventana.title("Etiquetas")
ventana.geometry("800x600")
ventana.config(background="#cccccc")
ventana.resizable(False,False)
ventana.iconphoto(True,PhotoImage(file="../images/python_icon.png"))

# Crear etiqueta
etiqueta = Label(ventana, text="Hola esta es una etiqueta...")


# pintar ventana
ventana.mainloop()