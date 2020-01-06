import sqlite3

miConexion = sqlite3.connect("primeraBase")

miCursor = miConexion.cursor() # Puntero o cursor

# LAS TRES COMILLAS DE ABAJO SIRVEN PARA PODER ESCRIBIR LA CONSULTA EN VARIAS LINEAS
# miCursor.execute(''' 
# 	CREATE TABLE productos(
# 	codigo_articulo VARCHAR(4) PRIMARY KEY,
# 	nombre_articulo VARCHAR(50),
# 	precio INTEGER,
# 	SECCION VARCHAR(20))
# 	''')

productos = [
	("AR05", "Pelota", 20, "Juguetería"),
	("AR06", "Pantalon", 15, "Confección"),
	("AR07", "Destornillador", 25, "Ferretería"),
	("AR08", "Jarron", 45, "Cerámica")
]

miCursor.executemany("INSERT INTO productos VALUES (?,?,?,?)", productos)

miConexion.commit()
miConexion.close()