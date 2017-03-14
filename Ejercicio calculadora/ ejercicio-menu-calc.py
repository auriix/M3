# coding: utf-8

print "Qué desea hacer el amo?"
print "1.-Sumar"
print "2.-Restar"
print "3.-Multiplicar"
print "4.-Dividir"
print "5.-Salir"

num = input ("Elige una opción: ")
if num < 1 or num >5 :
	print "Error: Aquesta opció no existeix."

if num == 1 :
	x = input ("Inserta un num: ")
	y = input ("Inserta otro num: ")
	print "Resultat de la suma: ",(x+y)

if num == 2 :
	x = input ("Inserta un num: ")
	y = input ("Inserta otro num: ")
	print "Resultat de la resta: ",(x-y)
	
if num == 3 :
	x = input ("Inserta un num: ")
	y = input ("Inserta otro num: ")
	print "Resultat de la multiplicació: ",(x*y)
	
if num == 4 :
	x = input ("Inserta un num: ")
	y = input ("Inserta otro num: ")
	print "Resultat de la divisió: ",(x/y)
	
if num == 5 :
	print "Adèu!"
