#coding: utf-8
#Imports
import os
os.system('clear')
from random import randint 

#Variables 
salir = False

aleatori = randint (1,4)
num = randint (2,14)
aleatori2 = randint (1,4)
num2 = randint (2,14)


#Nivell 2

def maquina():
	
	if (aleatori2 == 1) :
		palo2 = "de picas"
	
	if (aleatori2 == 2) :
		palo2 = "de diamantes"

	if (aleatori2 == 3) :
		palo2 = "de treboles"
		
	if (aleatori2 == 4) :
		palo2 = "de corazones"
		
	
	if (num2 <= 10) :
		carta2 = num2

	if (num2 == 11) :
		carta2 = "J"

	if (num2 == 12) :
		carta2 = "Q"

	if (num2 == 13) :
		carta2 = "K"
		
	print "Màquina:", carta2, palo2
	return

def jugador():
	if (aleatori == 1) :
		palo = "de picas"
		
	if (aleatori == 2) :
		palo = "de diamantes"

	if (aleatori == 3) :
		palo = "de treboles"
		
	if (aleatori == 4) :
		palo = "de corazones"
		
	if (num <= 10) :
		carta = num

	if (num == 11) :
		carta = "J"

	if (num == 12) :
		carta = "Q"

	if (num == 13) :
		carta = "K"
	
	if (num == 14) :
		carta = "A"
		
	print "Tú:", carta, palo
	return
	

def	quiguanya():
	if (num == num2) :
		print "Empat"
	
	else :
		if (num > num2) :
			print "Guanya la màquina!!"
		else :
			print "Has guanyat!!"


#Nivell 1

maquina()
	
jugador()

quiguanya()


	
