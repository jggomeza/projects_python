import sqlite3

miConexion = sqlite3.connect("primeraBase")

miCursor = miConexion.cursor() # Puntero o cursor

# LAS TRES COMILLAS DE ABAJO SIRVEN PARA PODER ESCRIBIR LA CONSULTA EN VARIAS LINEAS
# miCursor.execute(''' 
# 	CREATE TABLE productos(
# 	id INTEGER PRIMARY KEY AUTOINCREMENT,
# 	nombre_articulo VARCHAR(50) UNIQUE,
# 	precio INTEGER,
# 	seccion VARCHAR(20))
# 	''') # CREATE

# productos = [
# 	("Pelota", 20, "Juguetería"),
# 	("Pantalon", 15, "Confección"),
# 	("Destornillador", 25, "Ferretería"),
# 	("Jarron", 45, "Cerámica")
# ]

# miCursor.executemany("INSERT INTO productos VALUES (NULL,?,?,?)", productos)

# miCursor.execute("SELECT * FROM productos WHERE seccion = 'Confección'") # READ
# miCursor.execute("UPDATE productos SET precio=35 WHERE nombre_articulo='Pelota'") # UPDATE
miCursor.execute("DELETE FROM productos WHERE ID=2") # DELETE

# miCursor.execute("SELECT * FROM productos WHERE seccion = 'Juguetería'")
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