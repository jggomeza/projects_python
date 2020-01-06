for i in range(2):
	print(f"valor de la variable {i}")

for i in range(5,7):
	print(i)

for i in range(5,14,3):
	print(i)


# -------------------------------------------------
valido = False
email = input("Introduce tu email:")

for i in range(len(email)):
	if email[i] == "@":
		valido = True

if valido:
	print("Email correcto!")
else:
	print("Email incorrecto!")