from tkinter import *

# Iniciacializar ventana
ventana = Tk()

# Propiedades de ventana
ventana.title("Mi primera ventana")
ventana.geometry("1024x768")
ventana.resizable(True,True)
ventana.config(background="#336699")
logo = PhotoImage(file="images/python_icon.png")
ventana.iconphoto(True,logo)

# Pintar ventana
ventana.mainloop()