import math

i = 1

while i<=10:
	print("Ejecución " + str(i))
	i+=1

print("Termino la ejecución del programa")

#------------------------------------------------------------------------------------------------------------
edad =int(input("Introduce tu edad: "))

while edad<0 or edad>100:
	print("Has introducido una edad incorrecta, vuelve a intentarlo!")
	edad=int(input("Introduce tu edad por favor:"))

print("Gracias por colaborar, puedes pasar!")
print("Edad del aspirante " + str(edad) )

#------------------------------------------------------------------------------------------------------------

print("Programa de calculo de raíz cuadrada")
numero = int(input("Introduce un número por favor: "))

intento = 0

while numero<0:
	print("No se puede hallar la raíz de un número negativo!")

	if intento==2:
		print("Has consumido demasiados intentos. El programa ha finalizado.")
		break;

	numero = int(input("Introduce un número por favor: "))
	if numero<0:
		intento += 1 

if intento < 2:
	solucion = math.sqrt(numero)

	print(f"La raíz de {numero} es igual a {solucion}")