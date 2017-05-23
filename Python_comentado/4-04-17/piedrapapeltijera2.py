#coding: utf-8
#Inicialitza variables.
num = 31
salir = False

#Inici del bucle.
while salir==False : #Condició d'entrada.
	#Torns de jugada del Jugador 1:
	
	if num%7 == 0 or num%7 == 1 :
		j1 = "tijera"
	
	elif num%7 == 2 or num%7 == 3 or num%7 == 6 :
		j1 = "piedra"
		
	elif num%7 == 4 or num%7 == 5 :
		j1 = "papel"
		
	#Torns de jugada del Jugador 2:	
	if num%5 == 0 or num%5 == 1 or num%5 == 2 :
		j2 = "papel"
	
	elif num%5 == 3 :
		j2 = "tijera"
		
	elif num%5 == 4 :
		j2 = "piedra"
	
	
	#Si tenen el mateix resultat:
	if (j1 == j2) :
		print num, "Empate"
	#Regles del joc.
	elif (j1 == "piedra" and j2 == "papel") or (j1 == "papel" and j2 == "tijera") or (j1 == "tijera" and j2 == "piedra") :
		print num, "Gana el Jugador 2."
		
	else :
		print num, "Gana el Jugador 1."
	
#Condició de sortida:
	if num == 57 :
		
		salir = True
#Increment de la variable.
	num = num + 1
