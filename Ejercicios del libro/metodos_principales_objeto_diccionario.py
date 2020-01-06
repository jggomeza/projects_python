# Métodos de eliminación-------------------------------------------------------------------------------------

# Vaciar un diccionario
# Método: clear()
diccionario = {"color": "violeta", "talle": "XS", "precio": 174.25}
print (diccionario)  # {'color': 'violeta', 'talle': 'XS', 'precio': 174.25}
diccionario.clear()
print (diccionario)  # {}

# Métodos de agregado y creación-----------------------------------------------------------------------------
# Copiar un diccionario
# Método: copy()
diccionario = {"color": "violeta", "talle": "XS", "precio": 174.25}
remera = diccionario.copy()
print("diccionario =",diccionario)  # {'color': 'violeta', 'talle': 'XS', 'precio': 174.25}
print("remera =",remera)  # {'color': 'violeta', 'talle': 'XS', 'precio': 174.25}
diccionario.clear()
print("diccionario =",diccionario)  # {}
print("remera =",remera)  # {'color': 'violeta', 'talle': 'XS', 'precio': 174.25}
print("")

musculosa = remera
print("remera =",remera)  # {'color': 'violeta', 'talle': 'XS', 'precio': 174.25}
print("musculosa =",musculosa)  # {'color': 'violeta', 'talle': 'XS', 'precio': 174.25}
remera.clear()
print("remera =",remera)  # {}
print("musculosa =",musculosa)  # {}
print("")

# Crear un nuevo diccionario desde las claves de una secuencia
# Método: dict.fromkeys(secuencia[, valor por defecto])
secuencia = ["color", "talle", "marca"]
diccionario1 = dict.fromkeys(secuencia)
print(diccionario1)  # {'color': None, 'talle': None, 'marca': None}
diccionario2 = dict.fromkeys(secuencia, 'valor x defecto')
print(diccionario2)  # {'color': 'valor x defecto', 'talle': 'valor x defecto', 'marca': 'valor x defecto'}
print("")

# Concatenar diccionarios
# Método: update(diccionario)
diccionario1 = {"color": "verde", "precio": 45}
diccionario2 = {"talle": "M", "marca": "Lacoste"}
diccionario1.update(diccionario2)
print(diccionario1)  # {'color': 'verde', 'precio': 45, 'talle': 'M', 'marca': 'Lacoste'}
print("")

# Establecer una clave y valor por defecto
# Método: setdefault(“clave”[, None|valor_por_defecto])
""" Si la clave no existe, la crea con el valor por defecto.
Siempre retorna el valor para la clave pasada como
parámetro. """
remera = {"color": "rosa", "marca": "Zara"}
clave = remera.setdefault("talle", "U")
print("clave1 =",clave)  # 'U'
print("remera =",remera)  # {'color': 'rosa', 'marca': 'Zara', 'talle': 'U'}
remera2 = remera.copy()
print("")

print("remera2 =",remera2)  # {'color': 'rosa', 'marca': 'Zara', 'talle': 'U'}
clave = remera2.setdefault("estampado")
print("clave2 =", clave)
print("remera2 =",remera2)  # {'color': 'rosa', 'marca': 'Zara', 'talle': 'U', 'estampado': None}
print("")

clave = remera2.setdefault("marca", "Lacoste")
print("clave3 =",clave)  # 'Zara'
print("remera =",remera2)  # {'color': 'rosa', 'marca': 'Zara', 'talle': 'U', 'estampado': None}
print("")

# Métodos de retorno-----------------------------------------------------------------------------------------

# Obtener el valor de una clave
# Método: get(clave[, “valor x defecto si la clave no existe”])
print(remera.get("color"))  # 'rosa'
print(remera.get("stock"))
print(remera.get("stock", "sin stock"))  # 'sin stock'
print("")

""" # Saber si una clave existe en el diccionario
# Método: has_key(clave)
existe = remera.has_key("precio")
print(existe)  # False
existe = remera.has_key("color")
print(existe)  # True """

""" # Obtener las claves y valores de un diccionario
# Método: iteritems() Alias: items()
diccionario = {'color': 'rosa', 'marca': 'Zara', 'talle': 'U'}
for clave, valor in diccionario.iteritems():
	print("El valor de la clave %s es %s" % (clave, valor))
	# Salida:
	# El valor de la clave color es rosa
	# El valor de la clave marca es Zara
    # El valor de la clave talle es U """

# Obtener las claves de un diccionario
# Método: keys()
diccionario = {'color': 'rosa', 'marca': 'Zara', 'talle': 'U'}
claves = diccionario.keys()
print(claves)  # ['color', 'marca', 'talle']

# Obtener los valores de un diccionario
# Método: values()
diccionario = {'color': 'rosa', 'marca': 'Zara', 'talle': 'U'}
valores = diccionario.values()
print(valores)  # ['rosa', 'Zara', 'U']

# Obtener la cantidad de elementos de un diccionario
""" Para contar los elementos de un diccionario, al igual que con las listas y tuplas, se utiliza
la función integrada len() """
diccionario = {'color': 'rosa', 'marca': 'Zara', 'talle': 'U'}
print(len(diccionario))  # 3