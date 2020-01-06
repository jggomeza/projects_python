from io import open

archivo_texto = open("archivo.txt", "r") # w=solo escritura; r=solo lectura; a=añadir o agregar texto; r+ = lectura y escritura

# print(archivo_texto.read(11)) # lee solo hasta la cantidad de caracteres indicada
# archivo_texto.seek(11) # Posiciona el puntero en la posición indicada
# print(archivo_texto.read()) # Imprime el texto hasta el caracter indicado.

#archivo_texto.seek(len(archivo_texto.read())/2) # se ubica en la mitad del archivo
archivo_texto.seek(0)

print(archivo_texto.read())

archivo_texto.close()
del(archivo_texto)