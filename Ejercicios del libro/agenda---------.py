# -*- coding: utf-8 -*-
# Creación de una agenda simple, en Python.
# Introducción a Python.

# Definimos un menú principal.
def menu():
	texto = u'''
AGENDA v0.0.1 - Taller CALDUM Febrero 2011
Agenda de contactos de personas.
Elige opción:
1) Alta.
2) Baja.
3) Modificación.
4) Listar.
5) Guardar.
0) Salir.
'''
	print(texto)
	opcion = input("Elige opción: ")

	#Devolvemos opción.
	return opcion

# Definimos una clase para implementar la persistencia.
# import cPickle
class persistencia(object):
	def nombre_clase(self):
		return str(self).split(' ')[0].split('.')[1]

def cargar(self, nombre_fichero = None):
	if nombre_fichero is None:
		nombre_fichero = self.nombre_clase()
	manejador_fichero = open(nombre_fichero,'r')
	objeto = cPickle.load(manejador_fichero)
	manejador_fichero.close()
	return objeto

def salvar(self, objeto, nombre_fichero = None):
	if nombre_fichero is None:
		nombre_fichero = self.nombre_clase()
	# Fichero que contendrá el objeto.
	manejador_fichero = open(nombre_fichero,'w')
	# Volcamos el objeto de memoria al fichero.
	cPickle.dump(self, manejador_fichero)
	# Cerramos fichero.
	manejador_fichero.close()

# Creamos una clase agenda.
class mi_agenda(persistencia):
	def __init__(self):
		self.__lista = []
	
	def alta(self, persona):
		nick = persona[0].lower().strip()
		for i in self.__lista:
			if i[0].lower().strip() == nick:
				print("%s ya existe" % (nick))
			return
		self.__lista.append(persona)
		print("Alta correcta")

def baja(self, nick):
	for i in self.__lista:
		if i[0].lower().strip() == nick.lower().strip():
			self.__lista.remove(i)
			print("%s se ha borrado" % (nick))
			return
	print("%s no existe" % (nick))

def modificacion(self, persona):
	nick = persona[0]
	for i in self.__lista:
		if i[0].lower().strip() == nick.lower().strip():
			self.__lista.remove(i)
			self.__lista.append(persona)
			print("%s se ha modificado" % (nick))
			return
	print("%s no existe")

def lista(self):
	return self.__lista

# Cargamos la agenda en memoria.
agenda = mi_agenda()
try: agenda = agenda.cargar()
except: pass


# Script principal de la aplicación.
while True:
	opcion = menu()
	
	# Salimos
	if opcion == '0':break
	
	# Alta.
	if opcion == '1':
		buffer_alta = []
		for i in ['Nick:','Nombre:','Apellidos:','Teléfono:']:
			dato = input(i)
			buffer_alta.append(dato)
		
		# Intentamos dar de alta.
		agenda.alta(buffer_alta)
	
	# Baja.
	if opcion == '2':
		nick = input('Nick:')
		agenda.baja(nick)
	
	# Modificación.
	if opcion == '3':
		buffer_modif = []
		for i in ['Nick:','Nombre:','Apellidos:','Teléfono:']:
			dato = input(i)
			buffer_modif.append(dato)
		
		# Intentamos modificar.
		agenda.modificacion(buffer_modif)
	
	# Listar.
	if opcion == '4':
		lista = agenda.lista()
		for i in lista: print(i)
	
	# Guardar.
	if opcion == '5':
		agenda.salvar(agenda)