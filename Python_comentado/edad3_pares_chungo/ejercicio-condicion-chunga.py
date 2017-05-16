# coding: utf-8

#Esperem a llegir una resposta numèrica, la associem a la variable "numero"
numero = input ("Inserta un número : ")

#Condició:
if (numero %2 == 0) and (numero >= -10 and numero <= 40) and (numero < 0):
	#Si es compleix la condició.
	print "Cumple las 3 condiciones."
else:
	#Si no es compleix la condició.
	print "No cumple las 3 condiciones."
