#coding: utf-8

import os
os.system('clear')

diccionari = { "1" :'1D',"2":'2D',"3":'3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD',
	      '1T', '2T', '3T', '4T', '5T', '6T', '7T', '8T', '9T', '10T', 'JT', 'QT', 'KT',
	      '1P', '2P', '3P', '4P', '5P', '6P', '7P', '8P', '9P', '10P', 'JP', 'QP', 'KP',
	      '1C', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC'}

from random import randint 
salir = False

while (salir==False) :
	
	random.choice(diccionari.keys())
	print "Màquina":
	diccionari.pop (random.choice)	
	


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
