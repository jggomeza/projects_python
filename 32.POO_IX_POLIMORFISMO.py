class Coche(object):
	def dezplazamiento(self):
		print("Me dezplazo utilizando cuatro ruedas")

class Moto(object):
	def dezplazamiento(self):
		print("Me dezplazo utilizando dos ruedas")

class Camion(object):
	def dezplazamiento(self):
		print("Me dezplazo utilizando seis ruedas")

def dezplazamientoVehiculo(vehiculo):
	vehiculo.dezplazamiento()

miVehiculo = Coche() # or Moto or Camion

dezplazamientoVehiculo(miVehiculo)