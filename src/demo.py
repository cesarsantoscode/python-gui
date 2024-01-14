from tkinter import *

# Inicialización de la ventana
ventana = Tk()

# Configurando características de la ventana
ventana.title("Es es mi primera ventana")
ventana.geometry("800x600")
ventana.resizable(False, False)
ventana.config(background="#007700")
imagen = PhotoImage(file="images/python_icon.png")
ventana.iconphoto(True, imagen)

# Pintar ventana
ventana.mainloop()