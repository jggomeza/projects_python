"""Métodos principales del objeto list"""

# Métodos de agregado----------------------------------------------------------------------------------------

# Agregar un elemento al final de la lista
# Método: append(“nuevo elemento”)
nombres_masculinos = ["Alvaro", "Jacinto", "Miguel", "Edgardo", "David"]
nombres_masculinos.append("Jose")
print(nombres_masculinos)  # ['Alvaro', 'Jacinto', 'Miguel', 'Edgardo', 'David', 'Jose']

# Agregar varios elementos al final de la lista
# Método: extend(otra_lista)
nombres_masculinos.extend(["Jose", "Gerardo"])
print(nombres_masculinos)  # ['Alvaro', 'Jacinto', 'Miguel', 'Edgardo', 'David', 'Jose', 'Jose', 'Gerardo']

# Agregar un elemento en una posición determinada
# Método: insert(posición, “nuevo elemento”)
nombres_masculinos.insert(0, "Ricky")
print(nombres_masculinos)  # ['Ricky', 'Alvaro', 'Jacinto', 'Miguel', 'Edgardo', 'David', 'Jose', 'Jose', 'Gerardo']

# Métodos de eliminación-------------------------------------------------------------------------------------

# Eliminar el último elemento de la lista
# Método: pop()
# Retorna: el elemento eliminado
nombres_masculinos.pop()  # 'Gerardo'
print(nombres_masculinos)  # ['Ricky', 'Alvaro', 'Jacinto', 'Miguel', 'Edgardo', 'David', 'Jose', 'Jose']

# Eliminar un elemento por su índice
# Método: pop(índice)
# Retorna: el elemento eliminado
nombres_masculinos.pop(3)  # 'Miguel'
print(nombres_masculinos)  # ['Ricky', 'Alvaro', 'Jacinto', 'Edgardo', 'David', 'Jose', 'Jose']

# Eliminar un elemento por su valor
# Método: remove(“valor”)
nombres_masculinos.remove("Jose")
print(nombres_masculinos)  # ['Ricky', 'Alvaro', 'Jacinto', 'Edgardo', 'David', 'Jose']

# Métodos de orden-------------------------------------------------------------------------------------------

# Ordenar una lista en reversa (invertir orden)
# Método: reverse()
nombres_masculinos.reverse()
print(nombres_masculinos) # ['Jose', 'David', 'Edgardo', 'Jacinto', 'Alvaro', 'Ricky']

# Ordenar una lista en forma ascendente
# Método: sort()
nombres_masculinos.sort()
print(nombres_masculinos)  # ['Alvaro', 'David', 'Edgardo', 'Jacinto', 'Jose', 'Ricky']

# Ordenar una lista en forma descendente
# Método: sort(reverse=True)
nombres_masculinos.sort(reverse=True)
print(nombres_masculinos)  # ['Ricky', 'Jose', 'Jacinto', 'Edgardo', 'David', 'Alvaro']

# Métodos de búsqueda----------------------------------------------------------------------------------------

# Contar cantidad de apariciones elementos
# Método: count(elemento)
nombres_masculinos = ["Alvaro", "Miguel", "Edgardo", "David", "Miguel"]  # Esto es una lista
print(nombres_masculinos.count("Miguel"))  # 2

nombres_masculinos = ("Alvaro", "Miguel", "Edgardo", "David", "Miguel")  # Esto es una tupla
print(nombres_masculinos.count("Miguel"))  # 2

# Obtener número de índice
# Método: index(elemento[, indice_inicio, indice_fin])
print(nombres_masculinos.index("Miguel"))  # 1
print(nombres_masculinos.index("Miguel", 2, 5))

# Anexo sobre listas y tuplas--------------------------------------------------------------------------------

# Conversión de tipos

"""En el conjunto de las funciones integradas de Python, podemos encontrar dos funciones
que nos permiten convertir listas en tuplas y viceversa.
Estas funciones pueden ser muy útiles cuando por ejemplo, una variable declarada como
tupla, necesita ser modificada en tiempo de ejecución, para lo cual, debe convertirse en
una lista puesto que las tuplas, son inmutables. Lo mismo sucede en el caso contrario:
una variable que haya sido declarada como lista y sea necesario convertirla en una
colección inmutable."""

tupla = (1, 2, 3, 4)  
print(tupla)  # (1, 2, 3, 4)
lista1 = list(tupla)
print(lista1)  # [1, 2, 3, 4]

lista = [1, 2, 3, 4]  
print(lista)  # [1, 2, 3, 4]
tupla1 = tuple(lista)
print(tupla1)  # (1, 2, 3, 4)

# Concatenación simple de colecciones
"""A diferencia de otros lenguajes, en Python es muy simple unir varias colecciones de un
mismo tipo. Simplemente, se requiere utilizar el operador suma (+) para lograrlo:"""
lista1 = [1, 2, 3, 4]
print(lista1)
lista2 = [3, 4, 5, 6, 7, 8]
print(lista2)
lista3 = lista1 + lista2
print(lista3)  # [1, 2, 3, 4, 3, 4, 5, 6, 7, 8]

tupla1 = (1, 2, 3, 4, 5)
print(tupla1)
tupla2 = (4, 6, 8, 10)
print(tupla2)
tupla3 = (3, 5, 7, 9)
print(tupla3)
tupla4 = tupla1 + tupla2 + tupla3
print(tupla4)  # (1, 2, 3, 4, 5, 4, 6, 8, 10, 3, 5, 7, 9)

# Valor máximo y mínimo
# Podemos obtener además, el valor máximo y mínimo tanto de listas como de tuplas:

print(max(tupla4))  # 10
print(max(tupla1))  # 5
print(min(tupla1))  # 1
print(max(lista3))  # 8
print(min(lista1))  # 1

# Contar elementos
"""Al igual que para contar caracteres en una string, disponemos de la función integrada
len() para conocer la cantidad de elementos en una lista o en una tupla:"""
print(len(lista3))  # 10
print(len(lista1))  # 4
print(len(tupla2))  # 4