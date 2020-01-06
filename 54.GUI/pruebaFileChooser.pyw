from tkinter import *
from tkinter import filedialog

window = Tk()
# window.title("Practica de creación de menu")

def abreFichero():
	fichero = filedialog.askopenfilename(title="Abrir", initialdir="C:/", filetypes=(("Ficheros de Excel", "*.xlsx"), ("Ficheros de texto", "*.txt"), ("Todos los ficheros", "*.*")))
	# print(fichero)

Button(window, text="Abrir fichero", command=abreFichero).pack()

window.mainloop()