# -*- coding: utf-8 -*-
import os # Es para manipular el sistema de archivos, las carpetas
import sys
import shutil # Para poder agregar un archivo css
from string import Template # Importar la carpeta donde esta la plantilla base

acentos = {'á':'&aacute;', 'é':'&eacute;', 'í':'&iacute;', 'ó':'&oacute;', 'ú':'&uacute;', 'ñ':'&ntilde;', 'Ñ':'&Ntilde;', 'ä':'&auml;', 'ë':'&euml;', 'ï':'&iuml;', 'ö':'&ouml;', 'ü':'&uuml;', 'Á':'&Aacute;', 'É':'&Aacute;', 'Í':'&Iacute;', 'Ó':'&Oacute;', 'Ú':'&Uacute;', 'Ä':'&Auml;', 'Ë':'&Euml;', 'Ï':'&Iuml;', 'Ö':'&Ouml;', 'Ü':'&Uuml;'}

plantilla = open('Template/plantilla.html')

src = Template(plantilla.read())
nombre = input("Ingrese su nombre: \n")
matricula = input("Ingrese su matricula: \n")

for i in acentos:
	matricula = matricula.replace(str(i), str(acentos[i]))
	nombre = nombre.replace(str(i), str(acentos[i]))

listaCalificaciones = []

continuar = True
while continuar:
	calificacion = input("Ingrese su calificación: \n")
	listaCalificaciones.append(calificacion)
	respuesta = input("Quieres parar de ingresar calificaciones [si]-[no]: \n")

	if respuesta == 'si':
		continuar = False

notas = str(listaCalificaciones)
datos = {'nombre':nombre, 'matricula':matricula, 'notas':notas}

result = src.substitute(datos)

try:
	os.mkdir("Estudiantes")
	filein2 = open("Estudiantes/"+str(matricula)+".html", "w")
	filein2.writelines(result)
	print("Creando una carpeta")
	print("Guardando archivo")
except OSError:
	if os.path.exists("Estudiantes"):
		filein2 = open("Estudiantes/"+str(matricula)+".html", "w")
		filein2.writelines(result)
		print("Guardando archivo")


while True:
	pregunta = input("Presione c si quiere continuar y s si quiere salir \n")
	if pregunta == 'c':
		os.system("Estudiantes.py")
	elif pregunta == 's':
		sys.exit()