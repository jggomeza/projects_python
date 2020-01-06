nombreUsuario = input("Introduce un nombre de Usuario: ")
print("El nombre es:", nombreUsuario.upper())
print("El nombre es:", nombreUsuario.lower())
print("El nombre es:", nombreUsuario.capitalize())


edad = input("Introducela la edad: ")
# print(edad.isdigit())

while(edad.isdigit() == False):
	print("Por favor, introduce un valor numérico")

	edad = input("Introducela la edad: ")


if(int(edad)<18):
	print("No puedes pasar!")
else:
	print("Puedes pasar!")