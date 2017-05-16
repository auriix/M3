#coding: utf-8

import os

os.system('clear')

valor1 = input ("Escribe un valor: ")
valor2 = input ("Escribe otro valor: ")

if valor1 > valor2 :
	print  "El primer valor es mayor."

else :
	if (valor1 == valor2 ) :
		print  "El primer valor es igual al segundo valor."
		
	else :
		print "El segundo valor es mayor."

