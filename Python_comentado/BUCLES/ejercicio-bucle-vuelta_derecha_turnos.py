#coding: utf-8

#Inicialització de les variables.
num = 1
turnos = 0
salir = False

#Entra al bucle.
while (salir==False) :
	
	#Condicions
	if (num%8==1 or num%8==2) :
		print "arriba"
		
	if (num%8==3 or num%8==4) :
		print "derecha"
	
	if (num%8==5 or num%8==6) :
		print "abajo"
	
	if (num%8==7 or num%8==0) :
		print "izquierda"
		
	if (num%8==0) :
		turnos = turnos + 1
	
	#Condició de sortida del bucle.
	if (turnos == 2) :
		salir = True
		
	#Increment de la variable num.	
	num = num + 1

