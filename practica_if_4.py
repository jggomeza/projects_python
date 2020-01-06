print("Programa de becas año 2017")

distancia_escuela=int(input("Introduce la distancia a la escuela en km:\n"))
print(distancia_escuela)

numero_hermanos=int(input("Introduce el número de hermanos en el centro:\n"))
print(numero_hermanos)

salario_familiar=int(input("Introduce salario anual bruto:\n"))
print(salario_familiar)

if (distancia_escuela>40 and numero_hermanos>2 or salario_familiar<20000):
	print("Tienes derecho a beca!")
else:
	print("No tienes derecho a beca!")
###################################################################################################

print("Asignaturas optativas año 2017")
print("Informática Gráfica - Pruebas de Software - Usabilidad y Accesibilidad")
asignatura=input("Escriba la asignatura escogida:\n")

#upper() <mayusculas

if asignatura.lower() in("informática gráfica","pruebas de software", "usabilidad y accesibilidad"):
	print("Asignatura elegida " + asignatura)
else:
	print("La asignatura escogida no esta disponible!")
