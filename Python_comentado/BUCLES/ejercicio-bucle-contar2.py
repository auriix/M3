#coding: utf-8

#Inicialització de les variables.
num = 1
limite = input ("Inserta el límite: ")
salir = False

#Entra al bucle.
while (salir == False) :
	print num
	
	#Condició de sortida, surt cuan arriba al limit escollit a la inicialització de variables.
	if (num == limite) :
		salir = True
  	#Increment de variable num.
	num = num + 1
