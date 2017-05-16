#coding: utf-8

#Condició del bucle.
salir = False

#Mentres es compleixi la condició anterior (bucle).
while (salir == False) :
	
	print ("Hola")
	
	#Espera a llegir una tecla (alfanumèric).
	tecla = raw_input ("Sal con s o S:")
	
	#Condició:
	if (tecla == "S" or tecla == "s" ) :
  		print ("Adiós")
		
		#Surt del bucle.
    		salir = True
