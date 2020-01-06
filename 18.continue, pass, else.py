for letra in "Python":
	
	if letra=="h":
		continue

	print("Viendo la letra: " +  letra)
#----------------------------------------------------------------------------------------------------------

nombre = "Pildoras Informáticas"
contador = 0

for i in nombre:
	if i == " ":
		continue

	contador += 1

print(contador)
#----------------------------------------------------------------------------------------------------------

# while True:
# 	pass
#------------------------------------------------------------------------------------------------------------

email = input("Introduce tu email, por favor: ")

for i in email:
	if i == "@":
		arroba = True
		break;
else:
	arroba = False

print(arroba)
