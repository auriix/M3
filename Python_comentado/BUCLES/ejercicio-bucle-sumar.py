#coding: utf-8

num = 1
total = 0
salir = False

while (salir == False) :
  print num
  
  if (num == 5) :
    salir = True
  
  total = total + num
  num = num + 1
  
print "Total: ", total
