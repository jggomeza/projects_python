while True:

	nombre = input("Introdzca un nombre de usuario: ")

	if 5<len(nombre)<13:
		if nombre.isalnum():
			print(nombre.isalnum())
			break;
		else:
			print("""El nombre de usuario puede contener solo letras y números, 
	no se permitencaracteres de espacio en blanco!""")

	elif len(nombre)<6:
		print("El nombre de usuario debe contener al menos 6 caracteres")
	else:
		print("El nombre de usuario no puede contener más de 12 caracteres")