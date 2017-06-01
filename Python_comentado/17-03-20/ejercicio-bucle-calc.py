#coding: utf-8

import os

os.system('clear')

salir = False

while (salir == False) :
		
	print "Qué desea hacer el amo?"
	print "S.-Salir"
	print "1.-Sumar"
	print "2.-Restar"
	print "3.-Multiplicar"
	print "4.-Dividir"


	num = raw_input ("Elige una opción: ")



	if ( num >= "1" and num <= "4" ) or num == "s" or num == "S" :
		
		if num == "1" :
			print "Has escogido la opción Sumar."
			
		if num == "2" :
			print "Has escogido la opción Restar."
			
		if num == "3" :
			print "Has escogido la opción Multiplicar."
		
		if num == "4" :
			print "Has escogido la opción Dividir."
			
		if num == "s" or num == "S" :
			print "Has escogido la opción Salir."
			salir = True

	else :
		print "Esa opcion no existe."
