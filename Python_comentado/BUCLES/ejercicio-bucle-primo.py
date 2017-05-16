 #coding: utf-8
	
#Inicialització de les variables.
num = input ("Inserta un número: ")
cont = num
ceros = 0
salir = False 

#Entra al bucle.
while (salir == False) :
	
#Condicions

	if (num%cont == 0) :
		#Increment de la variable 0.
		ceros = ceros + 1
		
	#Condició de sortida.
	if (cont == 1) :
		salir = True
		
  	#Disminució de la variable cont
	cont = cont - 1

if (ceros == 2) :
	print "És primo."
else :
	print "No és primo."
  
