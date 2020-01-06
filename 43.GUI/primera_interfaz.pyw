from tkinter import *

window = Tk() # Se crea una instancia de la clase Tk
window.title("Ventana de pruebas") # establece un titulo
# window.resizable(1, 1) #(false, false)
window.iconbitmap("php.ico") # agrega un icono a la ventana
# window.geometry("650x350") # establece el tamaño de la ventana
window.config(bg="aqua")

miFrame = Frame() # Creamos un nuevo frame
miFrame.pack() # Empaquetamos el frame
# miFrame.pack(side="right") # Adherimos el frame a la derecha
# miFrame.pack(side="right", anchor="n") # Adherimos el frame a la derecha y al norte
# miFrame.pack(fill="x") # El frame se expande horizontalmente
# miFrame.pack(fill="y", expand="true") # El frame se expande verticalmente
# miFrame.pack(fill="both", expand="true") # El frame se expande verticalmente y horizontalmente
miFrame.config(bg="red") # color de fondo del frame
miFrame.config(width="650", height="350") # se establecen las medidas del frame
miFrame.config(bd=35) # ancho del borde
miFrame.config(relief="sunken") # tipo de borde (groove, sunken)
miFrame.config(cursor="pirate") # tipo de cursor (hand2, pirate)

window.mainloop()

# Nota: todo lo que aplicamos al frame se lo podemos aplicar tambien a la raíz!