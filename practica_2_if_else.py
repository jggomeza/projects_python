print("Verificación de acceso")

edad_usuario=int(input("Introduce tu edad, por favor:\n"))

if edad_usuario < 18:
	print("No puede pasar!")
elif edad_usuario > 100:
	print("Edad incorrecta")
else:
	print("Puedes pasar!")

##################################################################
nota_alumnos=int(input("Introduce tu nota, por favor:\n"))

if nota_alumnos < 5:
	print("Insuficiente!")
elif nota_alumnos < 6:
	print("Suficiente!")
elif nota_alumnos < 7:
	print("Bien!")
elif nota_alumnos < 9:
	print("Notable!")
else:
	print("Sobresaliente!")

print("A finalizado el programa!")