#coding: utf-8


#Inicialització de les variables.
num = input ("Inserta un número: ")
cont = num - 1
ceros = 0
salir = False 

#Entra al bucle.
while (salir == False) :
	#Condicions.
	if (num%cont == 0) :
		ceros = ceros + 1
		
	#Condició de sortida del bucle.	
	if (cont == 2 or ceros >= 1) :
		salir = True
		
  	#Disminució de la variable cont.
	cont = cont - 1

if (ceros == 0) :
	print "És primo."
else :
	print "No és primo."
  
