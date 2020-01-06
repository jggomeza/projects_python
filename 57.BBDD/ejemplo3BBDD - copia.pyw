import sqlite3

miConexion = sqlite3.connect("primeraBase")

miCursor = miConexion.cursor() # Puntero o cursor

# LAS TRES COMILLAS DE ABAJO SIRVEN PARA PODER ESCRIBIR LA CONSULTA EN VARIAS LINEAS
# miCursor.execute(''' 
# 	CREATE TABLE productos(
# 	id INTEGER PRIMARY KEY AUTOINCREMENT,
# 	nombre_articulo VARCHAR(50),
# 	precio INTEGER,
# 	SECCION VARCHAR(20))
# 	''')

productos = [
	("Pelota", 20, "Juguetería"),
	("Pantalon", 15, "Confección"),
	("Destornillador", 25, "Ferretería"),
	("Jarron", 45, "Cerámica")
]

miCursor.executemany("INSERT INTO productos VALUES (NULL,?,?,?)", productos)

miCursor.execute("SELECT * FROM productos")

variosProductos = miCursor.fetchall()

for row in variosProductos:
	for column in range(len(row)):
		if (column == len(row)-1):
			print(row[column])
		else:
			print(row[column], end=" ")

miConexion.commit()
miConexion.close()