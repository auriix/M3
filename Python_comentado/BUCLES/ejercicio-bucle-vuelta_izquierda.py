#coding: utf-8

#Inicialització de les variables

num = 1
direccion = raw_input ("Eige D (derecha) o I (izquierda): ")
salir = False

# Entra al bucle.
while (salir==False) :
	
	#Condicions.
	if (num%8==1 or num%8==2) :
		print "arriba"
		
	if (num%8==3 or num%8==4) :
		if (direccion == "D") :
			print "derecha"
		else :
			print "izquierda"
	
	if (num%8==5 or num%8==6) :
		print "abajo"
	
	if (num%8==7 or num%8==0) :
		if (direccion == "D") :
			print "izquierda"
		else :
			print "derecha"
			
	#Condició de sortida del bucle.	
	if (num==8) :
		salir = True
		
	#Increment de la variable.
	num = num + 1
