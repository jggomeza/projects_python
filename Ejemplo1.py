d=5

def mensaje():  #FUNCIÓN SENCILLA, No se mostrara su contenido hasta que sea llamada
	print("Estamos aprendiendo Python!")
	print("Estamos aprendiendo instrucciones básicas")
	print("Poco a poco iremos avanzando")

#mensaje()
######################################################## FUNCIÓN QUE RECIBE PARAMETROS
def function(min, max):
	
	for i in range(min,max+1):
		print("a(",i,")")

function(1,2)
######################################################## FUNCION QUE RETORNA RESULTADOS
def suma():
	num1=5
	num2=7
	resul=num1+num2

	#print(num1+num2)
	return resul

print(suma())
####################################################### LISTAS(ARRAYS)

milista=["María", "Pepe", "Marta", "Antonio"]#Esto es una lista sencilla
print(milista[:])#Esta función imprime todo el contenido de la lista
milista[1]="Pepes"  # Modifica el elemento de indice uno
print(milista[:])

print(milista[3])#Esta función imprim l elemento q stá ubikdo n la posición #3 n este kso Antonio
print(milista[-1])#Esta función imprime el elemento -1 de derecha a izquierda

print(milista[0:2])#A partir de la posición 0 imprime 2 elementos
print(milista[2:])#A partir de la posición 2 imprime todos los elementos
milista.append("Sandra")#Agrega un elemento al final de la lista
print(milista[:])

milista.insert(2,"Juan")#En la posición 2 insertame este elemento y corre todos los espacio a la derecha
print(milista[:])

milista.extend(["Sandra","Ana","Lucía"])#Al final de la lista agrega todos estos elementos
print(milista[:])

#Imprime el num del indice correspondiente al elemento que se pasa como parametro
print(milista.index("María"))
#Imprime true si el elemento que se pasa como parametro se encuentra en la lista
print("Pepe" in milista)

milista.remove("Ana")#Remueve el elemento que se pasa como parametro de la lista
print(milista[:])

milista2=["Ricardo","Deinnis"]
milista3=milista+milista2#Une el contenido de milista con el de milista2
print(milista3[:]*3)#Imprime tres veces el contenido de milista3

milista.pop() #elimina el ultimo elemento de milista
print(milista[:])
####################################################
