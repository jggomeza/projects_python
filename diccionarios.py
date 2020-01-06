midiccionario={"Alemania":"Berlin","Francia":"Paris","Reino Unido":"Londres","España":"Madrid"}
print(midiccionario["Francia"])

midiccionario["Italia"]="Lisboa" #Añadir un nuevo elemento
print(midiccionario)

midiccionario["Italia"]="Roma" #Modificar un elemento
print(midiccionario)

del midiccionario["Reino Unido"] #Eliminar una pareja clave valor
print(midiccionario)

midiccionario2={"Alemania":"Berlin",23:"Jordan","Mosqueteros":3}
print(midiccionario2)

milista=["España", "Francia", "Reino Unido", "Alemania"]
midiccionario3={milista[0]:"Madrid", milista[1]:"Paris", milista[2]:"Londres", milista[3]:"Berlin"}
print(midiccionario3[milista[1]])
print(midiccionario3["Francia"])

midiccionario={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "anillos":(1991, 1992, 1993, 1996, 1997, 1998)}
print(midiccionario["anillos"])

midiccionario={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "anillos":{"temporadas":(1991, 1992, 1993, 1996, 1997, 1998)}}
print(midiccionario["anillos"])

print(midiccionario.keys())
print(midiccionario.values())
print(len(midiccionario))