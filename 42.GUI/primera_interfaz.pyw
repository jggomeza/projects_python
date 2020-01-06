from tkinter import *

window = Tk()
window.title("Ventana de pruebas") # establece un titulo
window.resizable(1, 1) #(false, false)
window.iconbitmap("php.ico") # agrega un icono a la ventana
window.geometry("650x350") # establece el tamaño de la ventana
window.config(bg="aqua")

window.mainloop()