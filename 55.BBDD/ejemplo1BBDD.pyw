import sqlite3

miConexion = sqlite3.connect("primeraBase")

miCursor = miConexion.cursor() # Puntero o cursor

# miCursor.execute("CREATE TABLE productos (nombre_articulo varchar(50), precio integer, seccion varchar(20))")

miCursor.execute("INSERT INTO productos VALUES('BALÓN', 15, 'DEPORTES')")
miConexion.commit()

miConexion.close()