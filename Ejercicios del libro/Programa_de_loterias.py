# -*- coding: utf-8 -*-
import random, os

def combinacion(num_ele, total_num, repetir = False, ordenar_resultado = True):
	elementos = []
	if num_ele > total_num and not repetir:
		print("No puedes sacar más valores de los que ya tienes!")
		return

	aux = num_ele
	while aux > 0:
		numero = int(random.uniform(1,total_num))
		if repetir:
			elementos.append(numero)
			aux = aux - 1
		else:
			if elementos.count(numero) == 0:
				elementos.append(numero)
				aux = aux - 1

	if ordenar_resultado:
		elementos.sort()
		print(elementos)

def menu():
	print('''
================================
MENU PRINCIPAL
================================
Este programa genera combinaciones
de juegos de azar. Elige el juego
que más te guste.
1) Lotería primitiva
2) Euromillones
9) Salir
''')
	opcion = input("")
	return opcion

def aplicacion():
	os.system('cls')
	opcion = ""
	while opcion != "9":
		opcion = menu()
		if opcion == "1":
			print("")
			print("Combinación para Lotería Primitiva: ")
			combinacion(6,49)
			print("")

		if opcion == "2":
			print("")
			print("Euromillones")
			print("Combinación ganadora: ")
			combinacion(5,50)
			print("Estrellas: ")
			combinacion(2,9)
			print("")

# Ejecutamos el programa.
aplicacion()