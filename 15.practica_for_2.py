for i in ['Pildoras','Informaticas',1]:
	print("Hola", end=" ")

for i in "juan@ildorasinformaticas.es":
	print("Hola", end=" ")

email = False
miemail=input("Introduce tu direccion de email:")

for i in miemail:
	if (i=="@"):
		email = True

if email:
	print("")
	print("El email es correcto!")
else:
	print("El email no es correcto!")

for i in range(1,10):
	print(i)