from tkinter import *

window = Tk()
window.title("Ejemplo")

playa = IntVar()
montagna = IntVar()
turismoRural = IntVar()

def opcionesViaje():
	opcionEscojida = ""
	if (playa.get() == 1):
		opcionEscojida += " playa"
	if (montagna.get() == 1):
		opcionEscojida += " montaña"
	if (turismoRural.get() == 1):
		opcionEscojida += " turismoRural"
	textoFinal.config(text=opcionEscojida)

foto = PhotoImage(file="mouse.png")
Label(window, image=foto).pack()

frame = Frame(window)
frame.pack()

Label(frame, text="Elige estinos", width=50).pack()

Checkbutton(frame, text="Playa", variable=playa, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="Montaña", variable=montagna, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="Turismo rural", variable=turismoRural, onvalue=1, offvalue=0, command=opcionesViaje).pack()

textoFinal = Label(frame)
textoFinal.pack()

window.mainloop()