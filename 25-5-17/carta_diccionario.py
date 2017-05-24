#coding: utf-8
#Imports
import os
os.system('clear')
import random

cartas = {'1': , '2': ,'3': , '4': ,'5': , '6': ,'7': , '8': ,'9': , '10': ,'11': , '12': ,'13': , '14': }
palo = = {'1': , '2': ,'3': , '4': }

maquina = random.choice(cartas.keys()) + random.choice(palo.keys())
jugador = random.choice(cartas.keys()) + random.choice(palo.keys())

print "Màquina: " + maquina 
print "Jugador: " + jugador

if (num == num2) :
	print "Empat"
else :
	if (num > num2) :
		print "Guanya la màquina!!"
	else :
		print "Has guanyat!!"
		

if (num <> num2) :
	salir = True
