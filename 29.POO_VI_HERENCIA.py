class Vehiculos():
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

class Moto(Vehiculos):
	pass

miMoto = Moto("Honda", "CBR")

miMoto.estado()
		