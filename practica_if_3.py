edad=7

if 0<edad<100:
	print("Edad es correcta")
else:
	print("Edad Incorrecta")

################################

salario_presidente=int(input("Introduzca salario presidente:\n"))
print("Salario presidente " + str(salario_presidente))

salario_director=int(input("Introduzca salario director:\n"))
print("Salario director " + str(salario_director))

salario_jefe_area=int(input("Introduzca salario jefe de área:\n"))
print("Salario jefe de área " + str(salario_jefe_area))

salario_administrativo=int(input("Introduzca salario administrativo:\n"))
print("Salario administrativo " + str(salario_administrativo))

if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
	print("Todo funciona correctamente!")
else:
	print("Algo falla en esta empresa!")