mitupla=("Juan",13,1,1995,13)
print(mitupla[2])

milista=list(mitupla)
print(milista)

mitupla=tuple(milista)
print(mitupla)

print("Juan" in mitupla)

print(mitupla.count(13))  # Imprime cuantas veces se encuentra el elemento que se pasa como parentesis

#Imprime la cantidad de elementos que tiene mitupla
print(len(mitupla))

mitupla2=("Juan",)#tupla unitaria
print(len(mitupla2))

#Tambien se puede crear las tuplas sin usar los parentesis
mitupla3="Juan", 13, 1, 1995
print(mitupla3[:])

#Desempaquetado de tupla, asigna el contenido de cada indice a una variable
nombre, dia, mes, anio=mitupla3
print(nombre)
print(dia)
print(mes)
print(anio)

#Imprime el num del indice correspondiente al elemento que se pasa como parametro
print(mitupla3.index(13))
