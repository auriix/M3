#coding: utf-8
#Imports
import os
import random

#clear
os.system('clear')

#Variables
salir = False
cartas = {'1': , '2': ,'3': , '4': ,'5': , '6': ,'7': , '8': ,'9': , '10': ,'11': , '12': ,'13': , '14': }
palo = = {'1': , '2': ,'3': , '4': }

while (salir==False) do

	maquina = random.choice(cartas.keys()) 
	jugador = random.choice(cartas.keys()) 

	print "Màquina: " + maquina + random.choice(palo.keys())
	print "Jugador: " + jugador + random.choice(palo.keys())

	if (maquina == jugador) :
		print "Empat"
	else :
		if (maquina > jugador) :
			print "Guanya la màquina!!"
		else :
			print "Has guanyat!!"


	if (maquina <> jugador) :
		salir = True
