#coding: utf-8

salir = False

while (salir == False) :
	
	print ("Hola")
	
	tecla = raw_input ("Sal con s o S:")
	
	if (tecla == "S" or tecla == "s" ) :
		print ("Adiós")
		salir = True
