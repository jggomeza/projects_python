"""
	RANGOS
"""
import re

lista_nombres = ['Ana',
				'Pedro',
				'María',
				'Rosa',
				'Sandra',
				'Celia']

# for elemento in lista_nombres:
# 	if re.findall('[o-t]', elemento): # [o-t] lista todos los nombres que contengan este rango de letras en su interior
# 		print(elemento)

# for elemento in lista_nombres:
# 	if re.findall('^[O-T]', elemento): # ^[O-T] lista todos los nombres que comiencen con una letra en este rango
# 		print(elemento)

# for elemento in lista_nombres:
# 	if re.findall('[o-t]$', elemento): # [o-t]$ lista todos los nombres que terminen con una letra en este rango
# 		print(elemento)

lista_nombres = ['Ma1',
				'Se1',
				'Ma2',
				'Ba1',
				'Ma3',
				'Va1',
				'Va2',
				'Ma4',
				'MaA',
				'Ma5',
				'MaB',
				'MaC']

# for elemento in lista_nombres:
# 	if re.findall('Ma[0-3]', elemento): # Ma[0-3] lista todos los nombres que terminen en un rango de 0 a 3
# 		print(elemento)

# for elemento in lista_nombres:
# 	if re.findall('Ma[^0-3]', elemento): # Ma[^0-3] rango negado, muestra todo lo contrario que la anterior 
# 		print(elemento)

for elemento in lista_nombres:
	if re.findall('Ma[0-3A-B]', elemento): # Ma[0-3A-B] muestra todos los que comiencen con Ma y q l siga un rango comprendido entre 0-3A-B
		print(elemento)