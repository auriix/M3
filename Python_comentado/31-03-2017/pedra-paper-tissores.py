#coding: utf-8
#Llegim l'elecció de cada jugador.
j1 = raw_input ("Jugador 1 Elige > piedra, papel o tijera: ")
j2 = raw_input ("Jugador 2 Elige > piedra, papel o tijera: ")

#Els comparem:
if (j1 == j2) :
	print "Empate"
else : #Regles del joc.
	if (j1 == "piedra" and j2 == "papel") or (j1 == "papel" and j2 == "tijera") or (j1 == "tijeras" and j2 == "piedra") :
		print "Gana el jugador 2."
	else :
		print "Gana el jugador 1."
