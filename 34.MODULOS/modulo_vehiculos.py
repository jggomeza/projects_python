class Vehiculos(object):
	def __init__(self, marca, modelo): # Constructor de la clase, es el que da el estado inicial
		self.marca = marca
		self.modelo = modelo
		self.enmarcha = False
		self.acelera = False
		self.frena = False
		
	def arrancar(self):
		self.enmarcha = True

	def acelerar(self):
		self.acelera = True

	def frenar(self):
		self.frena = True

	def estado(self):
		print("Marca:",self.marca,"\nModelo:",self.modelo,"\nEn marcha:",self.enmarcha,"\nAcelerando:",self.acelera,"\nFrenando:",self.frena)

class Furgoneta(Vehiculos):
	
	def carga(self, cargar):
		self.cargado = cargar

		if(self.cargado):
			return "La furgoneta está cargada"
		else:
			return "La furgoneta no está cargada"
		
class Moto(Vehiculos):
	hcaballito = ""

	def caballito(self):
		self.hcaballito = "Voy haciendo caballito"

	def estado(self):
		super().estado()
		print(self.hcaballito)

class VElectricos(Vehiculos):
	def __init__(self, marca, modelo):
		super().__init__(marca, modelo)
		self.autonomia = 100

	def cargarEnergia(self):
		self.cargando = True

class BicicletaElectrica(VElectricos):
	pass

"""miMoto = Moto("Honda", "CBR")
miMoto.arrancar()
miMoto.caballito()
miMoto.estado()

miFurgoneta = Furgoneta("Renault", "Kangoo")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))

miBici = BicicletaElectrica("Orbea", "HC1030")
miBici.estado()		"""