"""
	MATCH Y SEARCH
"""
import re

nombre1 = "Sandra López"
nombre2 = "Antonio Gómez"
nombre3 = "María López"
nombre4 = "Jara López"
nombre5 = "Lara López"
cadena1 = "lklklklk"
cadena2 = "12345"
cadena3 = "a673"

if re.match(".ara", nombre5, re.IGNORECASE): # comodin punto sustituye una letra
	print("Hemos encontrado el nombre!")
else:
	print("No lo hemos encontrado!")

if re.match("\d", cadena2): # \d busca un digito al comienzo de una cadena
	print("Hemos encontrado el numero!")
else:
	print("No lo hemos encontrado!")

if re.search("López", nombre1, re.IGNORECASE): # \d busca un digito al comienzo de una cadena
	print("Hemos encontrado el nombre!")
else:
	print("No lo hemos encontrado!")