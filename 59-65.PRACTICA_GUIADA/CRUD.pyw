from tkinter import *
from tkinter import messagebox
import sqlite3

# ----------------------FUNCIONES-------------------------------------
def conexionBBDD():
	miConexion = sqlite3.connect("usuarios")
	miCursor = miConexion.cursor()

	try:
		miCursor.execute('''
			CREATE TABLE datosUsuarios(
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			nombre_usuario VARCHAR(50),
			apellido VARCHAR(50),
			password VARCHAR(50),
			direccion VARCHAR(50),
			comentarios VARCHAR(100)
			)
		''')

		messagebox.showinfo("BBDD", "BBDD creada con éxito")
	except Exception as e:
		messagebox.showwarning("¡Atención!", "La BBDD ya existe!")

def salirAplicacion():
	valor = messagebox.askquestion("Salir", "¿Desea salir de la aplicación?") # SI Y NO
	if (valor == 'yes'):
		window.destroy()
	# valor = messagebox.askokcancel("Salir", "¿Desea salir de la aplicación?") # OK Y CANCEL
	# if (valor == True):
	# 	window.destroy()

def limpiarCampos():
	txtId.set("")
	txtNombre.set("")
	txtApellido.set("")
	txtPassword.set("")
	txtDireccion.set("")
	textoComentario.delete(1.0, END)

def insertReg():
	miConexion=sqlite3.connect("Usuarios")
	miCursor=miConexion.cursor()
	# miCursor.execute("INSERT INTO datosUsuarios VALUES(NULL, '"+txtNombre.get()+
	# 	"', '"+txtApellido.get()+
	# 	"', '"+txtPassword.get()+
	# 	"', '"+txtDireccion.get()+
	# 	"', '"+textoComentario.get("1.0", END)+"')")

	datos = [
		txtNombre.get(), 
		txtApellido.get(), 
		txtPassword.get(), 
		txtDireccion.get(), 
		textoComentario.get("1.0", END)
		]

	miCursor.execute("INSERT INTO datosUsuarios VALUES (NULL,?,?,?,?,?)", (datos))
	miConexion.commit()
	limpiarCampos()
	messagebox.showinfo("BBDD", "Registro insertado con éxito!")

def selectReg():
	try:
		miConexion=sqlite3.connect("Usuarios")
		miCursor=miConexion.cursor()

		miCursor.execute("SELECT * FROM datosUsuarios WHERE id="+txtId.get())
		result = miCursor.fetchall()

		for row in result:
			txtId.set(row[0])
			txtNombre.set(row[1])
			txtApellido.set(row[2])
			txtPassword.set(row[3])
			txtDireccion.set(row[4])
			textoComentario.insert(1.0, row[5])

		miConexion.commit()
	except Exception as e:
		messagebox.showinfo("BBDD", "Introduzca un Id!")

def updateReg():
	miConexion=sqlite3.connect("Usuarios")
	miCursor=miConexion.cursor()
	# miCursor.execute("UPDATE datosUsuarios SET nombre_usuario='"+txtNombre.get()+
	# 	"', apellido='"+txtApellido.get()+
	# 	"', password='"+txtPassword.get()+
	# 	"', direccion='"+txtDireccion.get()+
	# 	"', comentarios='"+textoComentario.get("1.0", END)+
	# 	"' WHERE id="+txtId.get())

	datos = [
		txtNombre.get(), 
		txtApellido.get(), 
		txtPassword.get(), 
		txtDireccion.get(), 
		textoComentario.get("1.0", END)
		]

	miCursor.execute("UPDATE datosUsuarios SET nombre_usuario=?, apellido=?, password=?, direccion=?, comentarios=?" +
		"WHERE id="+txtId.get(), (datos))

	miConexion.commit()
	limpiarCampos()
	messagebox.showinfo("BBDD", "Registro actualizado éxitosamente!")

def deleteReg():
	valor = messagebox.askquestion("Eliminar", "¿Seguro que desea eliminar el registro?") # SI Y NO
	if (valor == 'yes'):
		miConexion=sqlite3.connect("Usuarios")
		miCursor=miConexion.cursor()
		miCursor.execute("DELETE FROM datosUsuarios WHERE id=" + txtId.get())

		miConexion.commit()
		limpiarCampos()
		messagebox.showinfo("BBDD", "El registro  se ha eliminado éxitosamente!")


# ---------------MAIN (INICIO DEL PROGRAMA)---------------------------------
window = Tk()
window.title("CRUD en Python aplicando todo lo aprendido") # establece un titulo
window.iconbitmap("php.ico") # agrega un icono a la ventana
window.resizable(0, 0) #(false, false)
# window.geometry("300x200") # establece el tamaño de la ventana

# --------------------MENU PRINCIPAL-----------------------------------
barraMenu = Menu(window)
window.config(menu=barraMenu, width=300, height=300)

bbddMenu = Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar", command=conexionBBDD)
bbddMenu.add_separator()
bbddMenu.add_command(label="Salir", command=salirAplicacion)
barraMenu.add_cascade(label="BBDD", menu=bbddMenu)

borrarMenu = Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar campos", command=limpiarCampos)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)

crudMenu = Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="Crear", command=insertReg)
crudMenu.add_command(label="Leer", command=selectReg)
crudMenu.add_command(label="Actualizar", command=updateReg)
crudMenu.add_command(label="Eliminar", command=deleteReg)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)

ayudaMenu = Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de")
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

#  ---------FRAME DE ENTRADA DE DATOS------------------------------
miFrame = Frame(window, width=1200, height=600)
miFrame.pack(fill="both", expand="true") # El frame se expande verticalmente y horizontalmente

txtId = StringVar()
txtNombre = StringVar()
txtApellido = StringVar()
txtPassword = StringVar()
txtDireccion = StringVar()

idLabel = Label(miFrame, text="Id:")
idLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)
campoId = Entry(miFrame, textvariable=txtId)
campoId.grid(row=0, column=1, padx=10, pady=10)

nombreLabel = Label(miFrame, text="Nombre:")
nombreLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)
campoNombre = Entry(miFrame, textvariable=txtNombre)
campoNombre.grid(row=1, column=1, padx=10, pady=10)

apellidoLabel = Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)
campoApellido = Entry(miFrame, textvariable=txtApellido)
campoApellido.grid(row=2, column=1, padx=10, pady=10)

PasswordLabel = Label(miFrame, text="Password:")
PasswordLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)
campoPassword = Entry(miFrame, textvariable=txtPassword)
campoPassword.grid(row=3, column=1, padx=10, pady=10)
campoPassword.config(show="*", justify="center")

direccionLabel = Label(miFrame, text="Dirección:")
direccionLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)
campoDireccion = Entry(miFrame, textvariable=txtDireccion)
campoDireccion.grid(row=4, column=1, padx=10, pady=10)

comentariosLabel = Label(miFrame, text="Comentarios:")
comentariosLabel.grid(row=5, column=0, sticky="e", padx=10, pady=10)
textoComentario = Text(miFrame, width=16, height=5)
textoComentario.grid(row=5, column=1, padx=10, pady=10)
scrollVertical = Scrollbar(miFrame, command=textoComentario.yview)
scrollVertical.grid(row=5, column=2, sticky="nsew")
textoComentario.config(yscrollcommand=scrollVertical.set)


#  ------------------------------------FRAME DE BOTONES------------------------------
miFrame2 = Frame(window, width=1200, height=600)
miFrame2.pack(fill="both", expand="true") # El frame se expande verticalmente y horizontalmente

botonCreate = Button(miFrame2, text="Create", command=insertReg)
botonCreate.grid(row=0, column=0, sticky="e", padx=10, pady=10)

botonRead = Button(miFrame2, text="Read", command=selectReg)
botonRead.grid(row=0, column=1, sticky="e", padx=10, pady=10)

botonUpdate = Button(miFrame2, text="Update", command=updateReg)
botonUpdate.grid(row=0, column=2, sticky="e", padx=10, pady=10)

botonDelete = Button(miFrame2, text="Delete", command=deleteReg)
botonDelete.grid(row=0, column=3, sticky="e", padx=10, pady=10)

window.mainloop()