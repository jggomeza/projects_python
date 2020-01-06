"""
	METAARACTERES (CARACTERES COMODÍN)
"""
import re

lista_nombres = ['Ana Gómez',
				'Maria Martín',
				'Sandra Lopez',
				'Santiago Martín',
				'Sandra Fernández']

# for elemento in lista_nombres:
# 	if re.findall('^Sandra', elemento): # ^ este metacaracter es para buscar aquellas cadenas que comiencen
# 		print(elemento)

# for elemento in lista_nombres:
# 	if re.findall('Martín$', elemento): # $ este metacaracter es para buscar aquellas cadenas que terminen
# 		print(elemento)

for elemento in lista_nombres:
	if re.findall('[ó]', elemento): # [] este metacaracter entre corchetes es para buscar aquellos caracteres dentro de una cadena
		print(elemento)

lista_nombres = ['Hombres',
				'Mujeres',
				'Mascotas',
				'Niños',
				'Niñas']

for elemento in lista_nombres:
	if re.findall('Niñ[oa]s', elemento): # [] este metacaracter entre corchetes es para buscar aquellos caracteres dentro de una cadena
		print(elemento)