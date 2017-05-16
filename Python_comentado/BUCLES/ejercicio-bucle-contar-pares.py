#coding: utf-8

#S'inicialitzen les variables.
num = 2
limite = input ("Escribe el límite: ")
salir = False

#Entra al bucle.
while (salir == False):
	if (num%2 == 0) :
		#Els numeros surten per pantalla sol si son pars.
  		print num
		
	#Condició de sortida.
	if (num == limite) :
		salir = True
		
  	#Increment de la variable.
	num = num + 1
