class Coche():
	def __init__(self): # Constructor de la clase, es el que da el estado inicial
		self.__largoChasis = 250 # Estas variables estan encapsuladas y no son accesibles desde fuera de la clase
		self.__anchoChasis = 120 # Estas variables estan encapsuladas y no son accesibles desde fuera de la clase
		self.__ruedas = 4 # Estas variables estan encapsuladas y no son accesibles desde fuera de la clase
		self.__enmarcha = False # Estas variables estan encapsuladas y no son accesibles desde fuera de la clase

	def arrancar(self, arrancamos): # Este es un compartamiento o metodo
		self.__enmarcha = arrancamos

		if(self.__enmarcha):
			chequeo = self.__chequeo_interno() # Llamada al metodo encapsulado

		if(self.__enmarcha and chequeo):
			return "El coche esta en marcha"
		elif(self.__enmarcha and chequeo == False):
			return "Algo ha ido mal en el chequeo. No podemos arrancar"
		else:
			return "El coche esta parado"

	def estado(self): # Este es otro compartamiento o metodo
		print("El coche tiene",self.__ruedas,"ruedas. Un ancho de",self.__anchoChasis,"y un largo de",self.__largoChasis)
	
	def __chequeo_interno(self): # Metodo encapsulado
		print("Realizando chequeo interno!")

		self.gasolina = "ok"
		self.aceite = "ok"
		self.puertas = "cerradas"

		if(self.gasolina == "ok" and  self.aceite == "ok" and self.puertas == "cerradas"):
			return True
		else:
			return False

miCoche = Coche() # Instancia de la clase Coche
print(miCoche.arrancar(True))
miCoche.estado()

print("---------A continuacion creamos el segundo objeto---------")
miCoche2 = Coche() # Instancia de la clase Coche
print(miCoche.arrancar(False))
miCoche2.estado()
#print(miCoche2.__chequeo_interno()) # Aunque lo llame con el mismo nombre no sera accesible porque esta encapsulado
