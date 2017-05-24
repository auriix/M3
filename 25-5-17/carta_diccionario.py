#coding: utf-8
#Imports
import os
import random

#clear
os.system('clear')

#Variables
salir = False
cartas = {'2': 2 ,'3': 3 , '4': 4 ,'5': 5 , '6': 6 ,'7': 7  , '8': 8 ,'9': 9 , '10': 10 , 'J': 11 , 'Q': 12,'K': 13, 'AS': 14 }
palo = {'Diamantes':"1", 'Picas':"2", 'Tréboles':"3", 'Corazones':"4"}

while (salir==False) :

	maquina = random.choice(cartas.keys()) 
	jugador = random.choice(cartas.keys()) 
	
	print "Màquina: ", maquina, random.choice(palo.keys())
	print "Jugador: ", jugador, random.choice(palo.keys())
	
	
	if (maquina == "J") :
		maquina = 11

	if (maquina == "Q") :
		maquina = 12

	if (maquina == "K") :
		maquina = 13
	
	if (maquina == "AS") :
		maquina = 14
	
	if (jugador == "J") :
		jugador = 11

	if (jugador == "Q") :
		jugador = 12

	if (jugador == "K") :
		jugador = 13
	
	if (jugador == "AS") :
		jugador = 14

	if (maquina == jugador) :
		print "Empat"
	else :
		if (maquina > jugador) :
			print "Guanya la màquina!!"
		else :
			print "Has guanyat!!"


	if (maquina <> jugador) :
		salir = True
