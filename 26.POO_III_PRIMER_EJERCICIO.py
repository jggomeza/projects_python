class Coche():
	largoChasis = 250
	anchoChasis = 120
	ruedas = 4
	enmarcha = False

	def arrancar(self): # Este es un compartamiento o metodo
		self.enmarcha = True

	def estado(self): # Este es otro compartamiento o metodo
		if(self.enmarcha):
			return "El coche esta en marcha"
		else:
			return "El coche esta parado"

miCoche = Coche() # Instancia de la clase Coche

print("El largo del coche es:", miCoche.largoChasis)
print("El coche tiene", miCoche.ruedas,"ruedas")
miCoche.arrancar()

print(miCoche.estado())
