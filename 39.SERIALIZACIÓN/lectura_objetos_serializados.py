import pickle
from serializar_objetos import *

ficheroApertura = open("loscoches", "rb")

misCoches = pickle.load(ficheroApertura)

ficheroApertura.close()
del(ficheroApertura)

for c in misCoches:
	c.estado()
	print("")