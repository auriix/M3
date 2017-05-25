#coding: utf-8
#Variables
salir = False
#Condició d'entrada al bucle.
while (salir == False) :
	#Print
	print ("Hola")
	#Read
	tecla = raw_input ("Sal con s o S:")
	#Condició de sortida del bucle.
	if (tecla == "S" or tecla == "s" ) :
		print ("Adiós")
		salir = True
