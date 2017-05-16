#coding: utf-8

#Inicialització de les variables.
num = 1
total = 0
salir = False

#Entra al bucle.
while (salir == False) :
  print num
  
  #Condició de sortida, (fa 5 prints : 1 2 3 4 5)
  if (num == 5) :
    salir = True
    
  #Increment de les variables. (1+2+3+4+5)
  total = total + num
  num = num + 1

#Surt per pantalla la suma total: 15
print "Total: ", total
