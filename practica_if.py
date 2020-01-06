print("Programa de evaluación de notas de alumnos")

nota_alumnos=input("Introduzca una calificación:\n")

def evaluacion(nota):
	valoracion="aprobado"

	if nota<5:
		valoracion="suspenso"
	return valoracion

print (evaluacion(int(nota_alumnos)))
