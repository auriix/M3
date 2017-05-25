# coding:utf-8
#Imports
import os
os.system('clear')
from random import randint 

#Variables
saldo = 100
apuesta = 0
salir_apuesta = False 	

#Surt per pantalla el teu saldo.
print "Tu saldo inicial:", saldo

#Condició d'entrada al bucle.		
while (salir_apuesta == False) :
	#Elegim la cantitat a apostar.
	apuesta = input ("Cantidad a apostar:")
	
	
	if (apuesta < 10 and apuesta >= 1) :
		print "El mínimo a apostar es 10"
		print ""
		
	#Condició de sortida del bucle.
	if (apuesta == -1) :
		print "Adiós"
		salir_apuesta = True
		
	#Si la cantitat introduïda per apostar es correcte establim la variable "salir" que ens servirà per entrar al següent bucle.
	if (apuesta > 10 and apuesta < saldo) :
		salir = False
		
		#Entrada del segon bucle.
		while (salir==False) :
			
			#Nombre aleatori per el pal de cada carta.
			aleatori = randint (1,4)
			if (aleatori == 1) :
				palo = "de picas"
				
			if (aleatori == 2) :
				palo = "de diamantes"

			if (aleatori == 3) :
				palo = "de treboles"
				
			if (aleatori == 4) :
				palo = "de corazones"
			

			#Nombre aleatori per el número de cada carta.
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
				carta = "AS"

			#Fem el mateix per la banca.
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
			
			#Resultats:
			print ""
			print "Banca:", carta, palo
			print "Yo:", carta2, palo2
			print ""

			#Qui guanya:
			if ( num > num2 or num == num2 ) :
				print "Gana la banca."
				#Si la banca guanya el teu saldo baixa.
				saldo = (saldo - apuesta)
				print "Tu saldo:", saldo
				#Surt del bucle de les jugades.
				salir = True
				
			if ( num < num2 ) :
				print "Ganas tú."
				#Si tu guanyes el teu saldo puja.
				saldo = (saldo + (apuesta * 2))
				print "Tu saldo:", saldo
				#Surt del bucle de les jugades.
				salir = True
	
	#Condició de sortida del primer bucle.
	if (salir == True ) :
		
			salir_apuesta = True


			
			
				
		
			
