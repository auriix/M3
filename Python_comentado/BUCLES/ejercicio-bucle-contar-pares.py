#coding: utf-8

num = 2
limite = input ("Escribe el límite: ")
salir = False

while (salir == False):
	if (num%2 == 0) :
  		print num
	
	if (num == limite) :
		salir = True
  
	num = num + 1
