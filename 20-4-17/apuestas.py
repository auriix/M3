# coding:utf-8
############################################################################
#                        QUE HACE?
# Saldo inicial: 100€
# Mínimo para apostar: 10€
# J1 Yo
# J2 Banca
############################################################################


############################################################################
#                        IMPORT
############################################################################

from random import randint 
import os

############################################################################
#                        VARIABLES GLOBALES
############################################################################

saldo = 100
apuesta = 0
salir_apuesta = False 	


############################################################################
#                               NIVEL 4
############################################################################



############################################################################
#                               NIVEL 3
############################################################################

def ifs_apuesta():
	if (apuesta == -1) :
		print "Adiós"
		salir_apuesta = True
		salir = False
	elif (apuesta < 10) :
		print "El mínimo a apostar es 10\n"
	if (apuesta > 10 and apuesta <= saldo) :
		
def palo_banca():
	if (aleatori == 1) :
		palo = "de picas"
		
	if (aleatori == 2) :
		palo = "de diamantes"

	if (aleatori == 3) :
		palo = "de treboles"
		
	if (aleatori == 4) :
		palo = "de corazones"

def carta_banca():
	if (num <= 10) :
		carta = num

	if (num == 11) :
		carta = "J"

	if (num == 12) :
		carta = "Q"

	if (num == 13) :
		carta = "K"
	
	if (num == 14) :
		carta = "AS"

def palo_yo():
	if (aleatori2 == 1) :
		palo2 = "de picas"
				
	if (aleatori2 == 2) :
		palo2 = "de diamantes"
		
	if (aleatori2 == 3) :
		palo2 = "de treboles"
				
	if (aleatori2 == 4) :
		palo2 = "de corazones"

def carta_yo():
	if (num2 <= 10) :
		carta2 = num2

	if (num2 == 11) :
		carta2 = "J"

	if (num2 == 12) :
		carta2 = "Q"

	if (num2 == 13) :
		carta2 = "K"
	
	if (num2 == 14) :
		carta2 = "AS"

############################################################################
#                               NIVEL 2
############################################################################

def apuesta():
	while (salir_apuesta == False) :
		apuesta = input ("Cantidad a apostar (-1 PARA SALIR) :")
		ifs_apuesta()

def banca():
	while (salir==False) :
		aleatori = randint (1,4)
		palo_banca()
		
		num = randint (2,14)
		carta_banca()
		
		print ""
		print "Banca:", carta, palo
		
def yo():
	while (salir==False) :
		aleatori2 = randint (1,4)
		palo_yo()
		
		num2 = randint (2,14)
		carta_yo()
		
		print "Yo:", carta2, palo2
		print ""
	

def ganador_banca():
	if ( num > num2 or num == num2 ) :
		print "Gana la banca."
		saldo = (saldo - apuesta)
		print "Tu saldo:", saldo
		print ""
		salir = True
	
def ganador_yo():
	if ( num < num2 ) :
		print "Ganas tú."
		saldo = (saldo + (apuesta * 2))
		print "Tu saldo:", saldo
		print ""
		salir = True
			

	
############################################################################
#                               NIVEL 1
############################################################################

os.system('clear')

#Mi apuesta
apuesta()

#Jugada de la banca
banca()

#Mi jugada
yo()

#Resultado
ganador_banca()
ganador_yo()



