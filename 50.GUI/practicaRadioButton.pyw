from tkinter import *

window = Tk()

varOpcion = IntVar()

def imprimir():
	# print(varOpcion.get())
	if varOpcion.get() == 1:
		etiqueta.config(text="Has elegido Masculino")
	elif varOpcion.get() == 2:
		etiqueta.config(text="Has elegido Femenino")
	else:
		etiqueta.config(text="Has elegido otras opciones")

Label(window, text="Genero:").pack()

Radiobutton(window, text="Masculino", variable=varOpcion, value=1, command=imprimir).pack()
Radiobutton(window, text="Femenino", variable=varOpcion, value=2, command=imprimir).pack()
Radiobutton(window, text="Otras opciones", variable=varOpcion, value=3, command=imprimir).pack()

etiqueta = Label(window)
etiqueta.pack()

window.mainloop()