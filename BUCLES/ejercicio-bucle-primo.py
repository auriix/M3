 #coding: utf-8
 
num = input ("Inserta un número: ")
cont = num
ceros = 0
salir = False 
 
while (salir == False) :
	if (num%cont == 0) :
		ceros = ceros + 1
		
	if (cont == 1) :
		salir = True
  
	cont = cont + 1

if (ceros == 2) :
	print "És primo."
else :
	print "No és primo."
  
