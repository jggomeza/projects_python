# password="aK47@jjjjj"
password = input("Introdzca su password para ingresar al sistema: ")

minuscula=0
mayuscula=0
numero=0
noalphanum=0

if 7<len(password) and password.count(" ")==0:
	for i in password:
		if i.islower():
			minuscula += 1
		if i.isupper():
			mayuscula += 1
		if i.isdigit():
			numero += 1
		if not(i.isalnum()):
			noalphanum += 1
	# print(minuscula)
	# print(mayuscula)
	# print(numero)
	# print(noalphanum)

	if 1<=minuscula and 1<=mayuscula and 1<=numero and 1<=noalphanum:
		resul = 1<=minuscula and 1<=mayuscula and 1<=numero and 1<=noalphanum
		print(resul," La contraeña ingresada es correcta!")
	else:
		if not(1<=minuscula):
			print("La contraseña ingresada debe contener al menos un caracter en minuscula!")
		if not(1<=mayuscula):
			print("La contraseña ingresada debe contener al menos un caracter en mayuscula!")
		if not(1<=numero):
			print("La contraseña ingresada debe contener al menos un número!")
		if not(1<=noalphanum):
			print("La contraseña ingresada debe contener al menos un caracter no alfanumerico!")
elif password.count(" ") > 0:
	print("No se permite el uso de espacios en blanco!")
else:
	print("La contraseña ingresada no cumple con la longitud adecuada >= 8 caracteres!")

	