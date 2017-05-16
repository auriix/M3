#coding: utf-8
 
num = input ("Inserta un número: ")
cont = num - 1
ceros = 0
salir = False 
 
while (salir == False) :
	if (num%cont == 0) :
		ceros = ceros + 1
		
	if (cont == 2 or ceros >= 1) :
		salir = True
  
	cont = cont - 1

if (ceros == 0) :
	print "És primo."
else :
	print "No és primo."
  
