#coding: utf-8

import os

os.system('clear')

print "Qué desea hacer el amo?"
print "S.-Salir"
print "1.-Sumar"
print "2.-Restar"
print "3.-Multiplicar"
print "4.-Dividir"


num = raw_input ("Elige una opción: ") 

if ( num >= "1" and num <= "4" ) or num == "s" or num == "S" :
	
	if num == "1" :
		x = input ("Inserta un num: ")
		y = input ("Inserta otro num: ")
		print "Resultat de la suma: ",(x+y)

	if num == "2" :
		x = input ("Inserta un num: ")
		y = input ("Inserta otro num: ")
		print "Resultat de la resta: ",(x-y)
		
	if num == "3" :
		x = input ("Inserta un num: ")
		y = input ("Inserta otro num: ")
		print "Resultat de la multiplicació: ",(x*y)
		
	if num == "4" :
		x = input ("Inserta un num: ")
		y = input ("Inserta otro num: ")
		print "Resultat de la divisió: ",(x/y)

	if num == "s" or num == "S" :
		print "Adiós."

else :
	print "Esa opcion no existe."
