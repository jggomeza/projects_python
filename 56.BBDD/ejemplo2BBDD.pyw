import sqlite3

miConexion = sqlite3.connect("primeraBase")

miCursor = miConexion.cursor() # Puntero o cursor

# variosProductos = [
# 	("Camiseta", 10, "Deportes"),
# 	("Jarron", 90, "Cerámica"),
# 	("Camion", 20, "Juguetería")
# ]

# miCursor.executemany("INSERT INTO productos VALUES(?,?,?)", variosProductos)

miCursor.execute("SELECT * FROM productos")

variosProductos = miCursor.fetchall()

for row in variosProductos:
	tamaño = 0
	for column in range(len(row)):
		if (column == 2):
			print(row[column])
		else:
			print(row[column], end=" ")

miConexion.commit()
miConexion.close()