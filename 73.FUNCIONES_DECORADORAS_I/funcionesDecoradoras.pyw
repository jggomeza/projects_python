def funcion_decoradora(funcionParametro):
	def funcionInterior():
		# Acciones adicionales que decoran
		print("Vamos a realizar un cálculo")
		funcionParametro()
		# Acciones adicionales que decoran
		print("Hemos terminado el cálculo")

	return funcionInterior

@funcion_decoradora
def suma():
	print(15+20)

@funcion_decoradora
def resta():
	print(30-10)

suma()
resta()