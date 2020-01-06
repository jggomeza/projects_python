# -*- coding: utf-8 -*-

import sys
import keyword


print("Palabras clave ", keyword.kwlist)

print(sys.platform)
print(sys.path)

tab = '\t'
enter = '\n'
contador = 1
cadena = ''
for i in keyword.kwlist:
	cadena += i + tab
	
	if contador == 5:
		contador = 1
		cadena += enter
	else:
		contador += 1

print(cadena)