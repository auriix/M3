#coding: utf-8
#Imports
import os
os.system ('clear')
from random import randint

#Jugador
#Esperem a llegir el teclat:
j1 = raw_input ("Jugador 1 > Elige piedra, papel, tijera, lagarto o spock :")

#Màquina
#Generem un número random del 1 al 5.
aleatori = randint (1,5)

if (aleatori == 1) :
	j2 = "piedra"

if (aleatori == 2) :
	j2 = "papel"

if (aleatori == 3) :
	j2 = "tijera"

if (aleatori == 4) :
	j2 = "lagarto"

if (aleatori == 5) :
	j2 = "spock"

print "La máquina elige:", j2

if (j1 == j2 ) :
	print "Empate"
else : #Regles del joc.
	if (j1 == "piedra" and (j2 == "lagarto" or j2 == "tijera")) or (j1 == "papel" and (j2 == "piedra" or j2 == "spock"))or (j1 == "tijera" and (j2 == "papel" or j2 == "lagarto")) or (j1 == "lagarto" and (j2 == "papel" or j2 == "spock")) or (j1 == "spock" and (j2 == "piedra" or j2 == "tijera")) :
		print "Gana el Jugador 1."
	else :
		print "Gana el Jugador 2."
	
