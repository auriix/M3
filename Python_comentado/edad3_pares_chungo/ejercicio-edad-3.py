#coding: utf8

#Esperem a llegir una resposta numèrica, la associem a la variable "edad"
edad = input ("Inserta tu edad: ")

#Condició:
if (edad >= 18 and edad <=23) or (edad == 17) or (edad >= 65 and edad <= 72) :
	#Si es compleix la condició.
	print "Puedes entrar en la sesión de jóvenes."
else:
	#Si no es compleix la condició.
	print "No puedes entrar en la sesión de jóvenes."
