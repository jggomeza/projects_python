class Coche():
	def __init__(self): # Constructor de la clase, es el que da el estado inicial
		self.__largoChasis = 250 # Estas variables estan encapsuladas y no son accesibles desde fuera de la clase
		self.__anchoChasis = 120 # Estas variables estan encapsuladas y no son accesibles desde fuera de la clase
		self.__ruedas = 4 # Estas variables estan encapsuladas y no son accesibles desde fuera de la clase
		self.__enmarcha = False # Estas variables estan encapsuladas y no son accesibles desde fuera de la clase

	def arrancar(self, arrancamos): # Este es un compartamiento o metodo
		self.__enmarcha = arrancamos

		if(self.__enmarcha):
			return "El coche esta en marcha"
		else:
			return "El coche esta parado"

	def estado(self): # Este es otro compartamiento o metodo
		print("El coche tiene",self.__ruedas,"ruedas. Un ancho de",self.__anchoChasis,"y un largo de",self.__largoChasis)
		

miCoche = Coche() # Instancia de la clase Coche
print(miCoche.arrancar(True))
miCoche.estado()

print("---------A continuacion creamos el segundo objeto---------")
miCoche2 = Coche() # Instancia de la clase Coche
print(miCoche.arrancar(False))
miCoche2.__ruedas = 5 # Aunque se coloque el nombre igual no se puede acceder a ella
miCoche2.estado()
