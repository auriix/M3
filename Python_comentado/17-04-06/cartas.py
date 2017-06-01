#coding: utf-8

#Importem la llibrería.
from random import randint 

#Generem número random del 1 al 4.
aleatori = randint (1,4)

#Si el numero generat es 1:
if (aleatori == 1) :
	palo = "de picas"
#Si el numero generat es 2:	
if (aleatori == 2) :
	palo = "de diamantes"
#Si el numero generat es 3:
if (aleatori == 3) :
	palo = "de treboles"
#Si el numero generat es 4:	
if (aleatori == 4) :
	palo = "de corazones"


#Generem número random del 1 al 13.
num = randint (1,13)

#Si el numero generat es menor o igual a 10:
if (num <= 10) :
	carta = num

#Si el numero generat es 11:
if (num == 11) :
	carta = "J"

	
#Si el numero generat es 12:
if (num == 12) :
	carta = "Q"

	
#Si el numero generat es 13:
if (num == 13) :
	carta = "K"


#Fem el mateix per l'altre jugador.
aleatori2 = randint (1,4)
if (aleatori2 == 1) :
	palo2 = "de picas"
	
if (aleatori2 == 2) :
	palo2 = "de diamantes"

if (aleatori2 == 3) :
	palo2 = "de treboles"
	
if (aleatori2 == 4) :
	palo2 = "de corazones"
	
num2 = randint (1,13)
if (num2 <= 10) :
	carta2 = num2

if (num2 == 11) :
	carta2 = "J"

if (num2 == 12) :
	carta2 = "Q"

if (num2 == 13) :
	carta2 = "K"

#El resultat de cada jugador:
print "Màquina:", carta, palo
print "Tú:", carta2, palo2

#Si el número generat de la primera carta es major que la segona: ¿Qui guanya?
if (num > num2) :
	print "La màquina guanya!!"
else :
	print "Has guanyat!!"
	
	
