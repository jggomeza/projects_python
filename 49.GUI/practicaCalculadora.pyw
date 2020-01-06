from tkinter import *

window = Tk()
window.title("Práctica Calculadora") # establece un titulo
window.iconbitmap("php.ico") # agrega un icono a la ventana
window.resizable(0, 0) #(false, false)
#window.geometry("200x200") # establece el tamaño de la ventana

miFrame = Frame(window)
miFrame.pack(fill="both", expand="true") # El frame se expande verticalmente y horizontalmente

operacion = "" # Variable global
resultado = 0 # Variable global

#------------------Pantalla---------------------------------------
numeroPantalla = StringVar()

pantalla = Entry(miFrame, textvariable=numeroPantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(background="black", fg="#03f943", justify="right", font=("Comic Sans MS", 11))

#---------------Pulsaciones Teclado-------------------------------

def numeroPulsado(num):
	global operacion

	if operacion == "":
		numeroPantalla.set(numeroPantalla.get() + num)
	else:
		numeroPantalla.set(num)
		operacion = ""

#---------------Funcion suma-------------------------------
def suma(num):
	global operacion
	global resultado

	resultado += int(num)
	operacion="suma"
	numeroPantalla.set(resultado)

#---------------Funcion resta-------------------------------
def resta(num):
	global operacion
	global resultado

	resultado -= int(num)
	operacion="resta"
	numeroPantalla.set(resultado)

#---------------Funcion el_resultado-------------------------------
def el_resultado():
	global resultado

	numeroPantalla.set(resultado + int(numeroPantalla.get()))
	resultado = 0
#------------------Fila 1-----------------------------------------

boton7 = Button(miFrame, text="7", width=6, height=3, command=lambda:numeroPulsado("7"))
boton7.grid(row=2, column=1)
boton8 = Button(miFrame, text="8", width=6, height=3, command=lambda:numeroPulsado("8"))
boton8.grid(row=2, column=2)
boton9 = Button(miFrame, text="9", width=6, height=3, command=lambda:numeroPulsado("9"))
boton9.grid(row=2, column=3)
botonDiv = Button(miFrame, text="/", width=6, height=3)
botonDiv.grid(row=2, column=4)

#------------------Fila 2-----------------------------------------

boton4 = Button(miFrame, text="4", width=6, height=3, command=lambda:numeroPulsado("4"))
boton4.grid(row=3, column=1)
boton5 = Button(miFrame, text="5", width=6, height=3, command=lambda:numeroPulsado("5"))
boton5.grid(row=3, column=2)
boton6 = Button(miFrame, text="6", width=6, height=3, command=lambda:numeroPulsado("6"))
boton6.grid(row=3, column=3)
botonMult = Button(miFrame, text="x", width=6, height=3)
botonMult.grid(row=3, column=4)

#------------------Fila 3-----------------------------------------

boton1 = Button(miFrame, text="1", width=6, height=3, command=lambda:numeroPulsado("1"))
boton1.grid(row=4, column=1)
boton2 = Button(miFrame, text="2", width=6, height=3, command=lambda:numeroPulsado("2"))
boton2.grid(row=4, column=2)
boton3 = Button(miFrame, text="3", width=6, height=3, command=lambda:numeroPulsado("3"))
boton3.grid(row=4, column=3)
botonRestar = Button(miFrame, text="-", width=6, height=3, command=lambda:resta(numeroPantalla.get()))
botonRestar.grid(row=4, column=4)


#------------------Fila 3-----------------------------------------

boton0 = Button(miFrame, text="0", width=6, height=3, command=lambda:numeroPulsado("0"))
boton0.grid(row=5, column=1)
botonComa = Button(miFrame, text=",", width=6, height=3, command=lambda:numeroPulsado("."))
botonComa.grid(row=5, column=2)
botonIgual = Button(miFrame, text="=", width=6, height=3, command=lambda:el_resultado())
botonIgual.grid(row=5, column=3)
botonSum = Button(miFrame, text="+", width=6, height=3, command=lambda:suma(numeroPantalla.get()))
botonSum.grid(row=5, column=4)

window.mainloop()