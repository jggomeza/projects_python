import doctest

def compruebaMail(mailUsuario):
	"""
	La función compruebaMail evalua un mail recibido en busca de la @.
	Si tiene una @ es correcto, si tiene más de una @ es incorrecto y
	si la @ está el final es incorrecto.

	>>> compruebaMail('juan@cursos.es')
	True

	>>> compruebaMail('juan@cursos.es@')
	False

	>>> compruebaMail('juancursos.es')
	False

	>>> compruebaMail('juan@cursos@.es')
	False
	"""

	arroba = mailUsuario.count('@')
	if(arroba!=1 or mailUsuario.rfind('@')==(len(mailUsuario)-1) or mailUsuario.find('@')==0):
		return False
	else:
		return True

# def areaTriangulo(base, altura):
	"""
	Cálcula el área de un triángulo dado
	
	>>> areaTriangulo(3, 6)
	'El área del triángulo es: 9.0'

	>>> areaTriangulo(4, 5)
	'El área del triángulo es: 10.0'

	>>> areaTriangulo(9, 3)
	'El área del triángulo es: 13.5'
	"""
	# return "El área del triángulo es: " + str((base*altura)/2)

# print(areaTriangulo(2,4))
doctest.testmod()