def suma(num1, num2):
	return num1 + num2

def resta(num1, num2):
	return num1 - num2

def multiplica(num1, num2):
	return num1 * num2

def divide(num1, num2):
	try:
		return num1 / num2
	except ZeroDivisionError:
		print("No se puede dividir entre cero!")
		return "Operacción errónea"

op1 = int(input("Introduce el primer número: "))
op2 = int(input("Introduce el segundo número: "))

opcion = int(input("Selecciona la operacion a realizar:\n1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir\n"))

if opcion==1:
	print(suma(op1, op2))
elif opcion==2:
	print(resta(op1, op2))
elif opcion==3:
	print(multiplica(op1, op2))
elif opcion==4:
	print(divide(op1, op2))
else:
	print("Operación no contemplada!")

print("Operacion ejecutada. Continuación de ejecución del programa...")

