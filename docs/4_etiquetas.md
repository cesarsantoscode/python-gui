[< Home](/README.md)

# 3. Etiquetas
Para crear etiquetas seguir los siguientes pasos:

* Para crear una ventana tenemos el siguiente código:
    ```python
    from tkinter import *

    ventana = Tk()
    ventana.title("Mi primera ventana")
    ventana.geometry("1024x768")
    ventana.resizable(False,False)
    ventana.config(background="#336699")
    logo = PhotoImage(file="../images/python_icon.png")
    ventana.iconphoto(True,logo)
    
    ventana.mainloop()
    ```