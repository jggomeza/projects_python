from tkinter import *

window = Tk() # Se crea una instancia de la clase Tk
window.title("Ventana de pruebas") # establece un titulo
window.iconbitmap("php.ico") # agrega un icono a la ventana
window.config(bg="aqua")

miFrame = Frame(window, width="500", height="400") # Creamos un nuevo frame
miFrame.pack() # Empaquetamos el frame

# miLabel = Label(miFrame, text="Hola alumnos de Python")
# miLabel.place(x="100", y="200")

# Label(miFrame, text="Hola alumnos de Python", fg="red", font=("Comic Sans MS", 18)).place(x="100", y="200")

miImagen =  PhotoImage(file="mouse.png")
Label(miFrame, image=miImagen).place(x="100", y="100")

window.mainloop()