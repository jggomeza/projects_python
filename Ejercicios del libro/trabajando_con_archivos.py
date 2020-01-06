archivo = open("texto.txt","a+")
contenido = archivo.read()

final_de_archivo = archivo.tell()
archivo.write("Nueva linea")
archivo.seek(final_de_archivo)
nuevo_contenido = archivo.read()
print(nuevo_contenido)
# Nueva linea