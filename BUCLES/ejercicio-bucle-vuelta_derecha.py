#coding: utf-8

num = 1
salir = False

while (salir==False) :
	if (num%8==1 or num%8==2) :
		print "arriba"
		
	if (num%8==3 or num%8==4) :
		print "derecha"
	
	if (num%8==5 or num%8==6) :
		print "abajo"
	
	if (num%8==7 or num%8==0) :
		print "izquierda"
		
	if (num==8) :
		salir = True
	
	num = num + 1
		
		
