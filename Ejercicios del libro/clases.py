class Antena():
	color = "negro"
	longitud = ""
class Pelo():
	color = ""
	textura = ""
class Ojo():
	forma = ""
	color = ""
	tamanio = ""
class Objeto():
	color = "verde"
	tamanio = "grande"
	aspecto = "feo"
	antenas = Antena() # propiedad compuesta por el objeto objeto Antena
	ojos = Ojo() # propiedad compuesta por el objeto objeto Ojo
	pelos = Pelo() # propiedad compuesta por el objeto objeto Pelo

	print(antenas.color)
	def flotar(self):
		print(12)

et = Objeto()
print(et.color)
print(et.tamanio)
print(et.aspecto)
et.color = "rosa"
print(et.color)
