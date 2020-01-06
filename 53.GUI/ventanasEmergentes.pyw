from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Practica de creación de menu")

def infoAdicional():
	messagebox.showinfo("Procesador de juan", "Procesador de textos version 2019")

def avisoLicencia():
	messagebox.showwarning("Licencia", "Producto bajo licencia GNU")

def salirAplicacion():
	# valor = messagebox.askquestion("Salir", "¿Desea salir de la aplicación?") # SI Y NO
	# if (valor == 'yes'):
	# 	window.destroy()

	valor = messagebox.askokcancel("Salir", "¿Desea salir de la aplicación?") # OK Y CANCEL
	if (valor == True):
		window.destroy()

def cerrarDocumento():
	valor = messagebox.askretrycancel("Reintentar", "No es posible cerrar. Documento bloqueado") # reintentar Y CANCEL

barraMenu = Menu(window)
window.config(menu=barraMenu, width=300, height=300)

archivoMenu = Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar", command=cerrarDocumento)
archivoMenu.add_command(label="Salir", command=salirAplicacion)

archivoEdicion = Menu(barraMenu, tearoff=0)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")

archivoHerramientas = Menu(barraMenu, tearoff=0)
archivoAyuda = Menu(barraMenu, tearoff=0)
archivoAyuda.add_command(label="Licencia", command=avisoLicencia)
archivoAyuda.add_command(label="Acerca de", command=infoAdicional)

barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edicion", menu=archivoEdicion)
barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)


window.mainloop()