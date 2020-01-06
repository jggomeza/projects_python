from io import open

archivo_texto = open("archivo.txt", "a") # w=solo escritura; r=solo lectura; a=añadir o agregar texto; r+ = lectura y escritura

"""frase = "Estupendo día para estudiar Python\nel miércoles"

archivo_texto.write(frase)

archivo_texto.close()
del(archivo_texto)"""

#texto = archivo_texto.read() # Lee todo el contenido del archivo

#texto = archivo_texto.readlines() # Lee linea a linea y almacena en una lista

#archivo_texto.close()
#del(archivo_texto)

archivo_texto.write("\nSiempre es una buena ocación para estudiar Python")

archivo_texto.close()
del(archivo_texto)