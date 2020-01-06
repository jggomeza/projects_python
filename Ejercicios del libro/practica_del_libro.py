# -*- coding: utf-8 -*-

# print ("En el Ñágara encontré un Ñandú")

# import Ejemplos_de_Python.Ejemplo1 as e  # Esto es un alias
# print(e.function(1,2))

#from Ejemplos_de_Python.Ejemplo1 import *
##from Ejemplo1 import *

#print(function(1,2))

def funcion():
	return "Hola Mundos!"

frase = funcion()
print(frase)

def mi_funcion(nombre, apellido):
	nombre_completo = nombre, apellido
	print(nombre_completo)

mi_funcion('José','Gómez')


def funcion():
	return "Hola Mundo"


# METÓDOS DE FORMATO DE CADENAS--------------------------------------------------------------------------------

# Convertir a mayúscula la primera letra
# Método: capitalize() 
# Retorna: una copia de la cadena con la primera letra en mayúsculas
cadena = "bienvenido a mi aplicación"
print(cadena.capitalize())  

# Convertir una cadena a minúsculas
# Método: lower() 
# Retorna: una copia de la cadena en minusculas
cadena = "Hola Mundo"
print(cadena.lower())  

# Convertir una cadena a mayúsculas
# Método: upper() 
# Retorna: una copia de la cadena en mayusculas
cadena = "Hola Mundo"
print(cadena.upper())  

# Convertir mayúsculas a minúsculas y viceversa
# Método: swapcase() 
# Retorna: una copia de la cadena convertidas las mayúsculas en minúsculas y viceversa
cadena = "Hola Mundo"
print(cadena.swapcase())  

# Convertir una cadena en Formato Título
# Método: title() 
# Retorna: una copia de la cadena convertida
cadena = "hola mundo"
print(cadena.title())

# Centrar un texto
# Método: center(longitud[, “caracter de relleno”])
# Retorna: una copia de la cadena centrada
cadena = "bienvenido a mi aplicación".capitalize()
print(cadena.center(50, "="))
print(cadena.center(50, " "))

# Alinear texto a la izquierda
# Método: ljust(longitud[, “caracter de relleno”])
# Retorna: una copia de la cadena alineada a la izquierda
cadena = "bienvenido a mi aplicación".capitalize()
print(cadena.ljust(50, "="))

# Alinear texto a la derecha
# Método: rjust(longitud[, “caracter de relleno”])
# Retorna: una copia de la cadena alineada a la derecha
cadena = "bienvenido a mi aplicación".capitalize()
print(cadena.rjust(50, "="))
print(cadena.rjust(50, " "))

# Rellenar un texto anteponiendo ceros
# Método: zfill(longitud)
# Retorna: una copia de la cadena rellena con ceros a la izquierda hasta alcanzar la longitud final indicada
numero_factura = 1575
print(str(numero_factura).zfill(6))

# METÓDOS DE BUSQUEDA-----------------------------------------------------------------------------------------

# Contar cantidad de apariciones de una subcadena
# Método: count(“subcadena”[, posicion_inicio, posicion_fin])
# Retorna: un entero representando la cantidad de apariciones de subcadena dentro de cadena
cadena = "bienvenido a mi aplicación".capitalize()
print(cadena.count("a"))

# Buscar una subcadena dentro de una cadena
# Método: find(“subcadena”[, posicion_inicio, posicion_fin])
# Retorna: un entero representando la posición donde inicia la subcadena dentro de 
# cadena. Si no la encuentra, retorna -1
cadena = "bienvenido a mi aplicación".capitalize()
print(cadena.find("mi"))
print(cadena.find("mi", 0, 10))

# Métodos de Validación--------------------------------------------------------------------------------------

# Saber si una cadena comienza con una subcadena determinada
# Método: startswith(“subcadena”[, posicion_inicio, posicion_fin]) 
# Retorna: True o False
cadena = "bienvenido a mi aplicación".capitalize()
print(cadena.startswith("Bienvenido"))  # True
print(cadena.startswith("aplicación"))  # False
print(cadena.startswith("aplicación", 16))  # True

# Saber si una cadena finaliza con una subcadena determinada
# Método: endswith(“subcadena”[, posicion_inicio, posicion_fin])
# Retorna: True o False
cadena = "bienvenido a mi aplicación".capitalize()
print(cadena.endswith("aplicación"))  # True
print(cadena.endswith("Bienvenido"))  # False
print(cadena.endswith("Bienvenido", 0, 10))  # True

# Saber si una cadena es alfanumérica
# Método: isalnum()
# Retorna: True o False
cadena = "pepegrillo 75"
print(cadena.isalnum())  # False
cadena = "pepegrillo"
print(cadena.isalnum())  # True
cadena = "pepegrillo75"
print(cadena.isalnum())  # True

# Saber si una cadena es alfabética
# Método: isalpha()
# Retorna: True o False
cadena = "pepegrillo 75"
print(cadena.isalpha())  # False
cadena = "pepegrillo"
print(cadena.isalpha())  # True
cadena = "pepegrillo75"
print(cadena.isalpha())  # False

# Saber si una cadena es numérica
# Método: isdigit()
# Retorna: True o False
cadena = "pepegrillo 75"
print(cadena.isdigit())  # False
cadena = "7584"
print(cadena.isdigit())  # True
cadena = "75 84"
print(cadena.isdigit())  # False
cadena = "75.84"
print(cadena.isdigit())  # False

# Saber si una cadena contiene solo minúsculas
# Método: islower()
# Retorna: True o False
cadena = "pepe grillo"
print(cadena.islower())  # True
cadena = "Pepe Grillo"
print(cadena.islower())  # False
cadena = "Pepegrillo"
print(cadena.islower())  # False
cadena = "pepegrillo75"
print(cadena.islower())  # True

# Saber si una cadena contiene solo mayúsculas
# Método: isupper()
# Retorna: True o False
cadena = "PEPE GRILLO"
print(cadena.isupper())  # True
cadena = "Pepe Grillo"
print(cadena.isupper())  # False
cadena = "Pepegrillo"
print(cadena.isupper())  # False
cadena = "PEPEGRILLO"
print(cadena.isupper())  # True

# Saber si una cadena contiene solo espacios en blanco
# Método: isspace()
# Retorna: True o False
cadena = "pepe grillo"
print(cadena.isspace())  # False
cadena = " "
print(cadena.isspace())  # True

# Saber si una cadena tiene Formato De Título
# Método: istitle()
# Retorna: True o False
cadena = "Pepe Grillo"
print(cadena.istitle())  # True
cadena = "Pepe grillo"
print(cadena.istitle())  # False

# Métodos de Sustitución-------------------------------------------------------------------------------------

# Dar formato a una cadena, sustituyendo texto dinámicamente
# Método: format(*args, **kwargs)
# Retorna: la cadena formateada
cadena = "bienvenido a mi aplicación {0}".capitalize()
print(cadena.format("en Python"))  # Bienvenido a mi aplicación en Python
cadena = "Importe bruto: ${0} + IVA: ${1} = Importe neto: {2}"
print(cadena.format(100, 21, 121) ) # Importe bruto: $100 + IVA: $21 = Importe neto: 121
cadena = "Importe bruto: ${bruto} + IVA: ${iva} = Importe neto: {neto}"
print(cadena.format(bruto=100, iva=21, neto=121))  # Importe bruto: $100 + IVA: $21 = Importe neto: 121
print(cadena.format(bruto=100, iva=100 * 21 / 100, neto=100 * 21 / 100 + 100))  # Importe bruto: $100 + IVA: $21 = Importe neto: 121

# Reemplazar texto en una cadena
# Método: replace(“subcadena a buscar”, “subcadena por la cual reemplazar”)
# Retorna: la cadena reemplazada
buscar = "nombre apellido"
reemplazar_por = "Juan Pérez"
print("Estimado Sr. nombre apellido:".replace(buscar, reemplazar_por))  # Estimado Sr. Juan Pérez:

# Eliminar caracteres a la izquierda y derecha de una cadena
# Método: strip([“caracter”])
# Retorna: la cadena sustituida
cadena = " www.eugeniabahit.com "
print(cadena.strip())  # www.eugeniabahit.com
print(cadena.strip(' '))  # www.eugeniabahit.com

# Eliminar caracteres a la izquierda de una cadena
# Método: lstrip([“caracter”])
# Retorna: la cadena sustituida
cadena = "www.eugeniabahit.com"
print(cadena.lstrip("w." ))  # eugeniabahit.com
cadena = " www.eugeniabahit.com"
print(cadena.lstrip())  # www.eugeniabahit.com

# Eliminar caracteres a la derecha de una cadena
# Método: rstrip([“caracter”])
# Retorna: la cadena sustituida
cadena = "www.eugeniabahit.com "
print(cadena.rstrip( ))  # www.eugeniabahit.com

# Métodos de unión y división--------------------------------------------------------------------------------

# Unir una cadena de forma iterativa
# Método: join(iterable)
# Retorna: la cadena unida con el iterable (la cadena es separada por cada uno de los
# elementos del iterable)
formato_numero_factura = ("Nº 0000-0", "-0000 (ID: ", ")")
numero = "275"
numero_factura = numero.join(formato_numero_factura)
print(numero_factura)  # Nº 0000-0275-0000 (ID: 275)

# Partir una cadena en tres partes, utilizando un separador
# Método: partition(“separador”)
"""Retorna: una tupla de tres elementos donde el primero es el contenido de la cadena
   previo al separador, el segundo, el separador mismo y el tercero, el contenido de la
   cadena posterior al separador"""
tupla = "http://www.eugeniabahit.com".partition("www.")
print(tupla)  # ('http://', 'www.', 'eugeniabahit.com')
protocolo, separador, dominio = tupla
print("Protocolo: {0}\nDominio: {1}".format(protocolo, dominio))  # Protocolo: http:// Dominio: eugeniabahit.com

# Partir una cadena en varias partes, utilizando un separador
# Método: split(“separador”)
# Retorna: una lista con todos elementos encontrados al dividir la cadena por un separador
keywords = "python, guia, curso, tutorial".split(", ")
print(keywords)  # ['python', 'guia', 'curso', 'tutorial']

# Partir una cadena en líneas
# Método: splitlines()
# Retorna: una lista donde cada elemento es una fracción de la cadena divida en líneas
texto = """Linea 1
Linea 2
Linea 3
Linea 4
"""
print(texto.splitlines())  # ['Linea 1', 'Linea 2', 'Linea 3', 'Linea 4']
texto = "Linea 1\nLinea 2\nLinea 3"
print(texto.splitlines())  # ['Linea 1', 'Linea 2', 'Linea 3']

print(len("1234567890"))  # Cuenta la cantidad de caracteres en una cadena