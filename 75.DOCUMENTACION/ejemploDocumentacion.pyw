"""Este modulo contiene la clase que permite cálcular el área de diferentes figuras geometricas"""
class Areas(object):
	"""Esta clase cálcula las areas de diferentes fíguras geométricas"""

	def areaCuadrado(lado):
		"""	Cálcula el área de un cuadrado elevando
		al cuadrado el lado pasado por parámetro"""

		return "EL área del cuadrado es: " + str(lado*lado)

	def areaTriangulo(base, altura):
		"""Cálcular el área de un triángulo utilizando los parámetros base y altura"""
		return "El área del triángulo es: " + str((base*altura)/2)

# print(Areas.areaCuadrado.__doc__)
# print(Areas.areaCuadrado(5))
# help(Areas.areaTriangulo)
# help(Areas)