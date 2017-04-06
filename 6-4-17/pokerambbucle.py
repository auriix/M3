#coding: utf-8

import os
os.system('clear')

from random import randint 
salir = False

while (salir==False) :

	aleatori = randint (1,4)
	if (aleatori == 1) :
		palo = "de picas"
		
	if (aleatori == 2) :
		palo = "de diamantes"

	if (aleatori == 3) :
		palo = "de treboles"
		
	if (aleatori == 4) :
		palo = "de corazones"
		
	num = randint (2,14)
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


	aleatori2 = randint (1,4)
	if (aleatori2 == 1) :
		palo2 = "de picas"
		
	if (aleatori2 == 2) :
		palo2 = "de diamantes"

	if (aleatori2 == 3) :
		palo2 = "de treboles"
		
	if (aleatori2 == 4) :
		palo2 = "de corazones"
		
	num2 = randint (2,14)
	if (num2 <= 10) :
		carta2 = num2

	if (num2 == 11) :
		carta2 = "J"

	if (num2 == 12) :
		carta2 = "Q"

	if (num2 == 13) :
		carta2 = "K"
	
	if (num2 == 14) :
		carta2 = "A"


	print "Màquina:", carta, palo
	print "Tú:", carta2, palo2

	if (num == num2) :
		print "Empat"
	else :
		if (num > num2) :
			print "Guanya la màquina!!"
		else :
			print "Has guanyat!!"
		

	if (num <> num2) :
		salir = True
		
