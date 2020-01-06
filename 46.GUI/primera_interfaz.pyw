from tkinter import *

window = Tk()
window.title("Ventana de pruebas") # establece un titulo
window.iconbitmap("php.ico") # agrega un icono a la ventana
window.resizable(0, 0) #(false, false)
# window.geometry("300x200") # establece el tamaño de la ventana

miFrame = Frame(window, width=1200, height=600)
miFrame.pack(fill="both", expand="true") # El frame se expande verticalmente y horizontalmente

miNombre = StringVar()

nombreLabel = Label(miFrame, text="Nombre:")
nombreLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)
campoNombre = Entry(miFrame, textvariable=miNombre)
campoNombre.grid(row=0, column=1, padx=10, pady=10)
campoNombre.config(fg="red", justify="center")

apellidoLabel = Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)
campoApellido = Entry(miFrame)
campoApellido.grid(row=1, column=1, padx=10, pady=10)

direccionLabel = Label(miFrame, text="Direccion:")
direccionLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)
campoDireccion = Entry(miFrame)
campoDireccion.grid(row=2, column=1, padx=10, pady=10)

passwordLabel = Label(miFrame, text="Password:")
passwordLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)
campoPassword = Entry(miFrame)
campoPassword.grid(row=3, column=1, padx=10, pady=10)
campoPassword.config(show="*", justify="center")

comentariosLabel = Label(miFrame, text="Comentarios:")
comentariosLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)
textoComentario = Text(miFrame, width=15, height=5)
textoComentario.grid(row=4, column=1, padx=10, pady=10)
scrollVertical = Scrollbar(miFrame, command=textoComentario.yview)
scrollVertical.grid(row=4, column=2, sticky="nsew")
textoComentario.config(yscrollcommand=scrollVertical.set)

def codigoBoton():
	miNombre.set("Juan")

botonEnvio = Button(window, text="Enviar", command=codigoBoton)
botonEnvio.pack()

window.mainloop()