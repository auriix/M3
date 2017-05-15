#coding: utf-8
import calendar


mes = input ("Inserta el mes (1-12): ") 
anyo = input ("Inserta el año (AAAA): ")
cont=1


num_dias_mes = calendar.monthrange(anyo, mes)
dia_semana = calendar.weekday(anyo, mes, 1)
tope = num_dias_mes
  

print "l m m j v s d"
print "-------------"

def my_range(inici, fi, increment):
    while inici <= fi:
        #Retorna l'element actual del rang (llista)
        yield inici
        inici = inici + increment

		
for fil in my_range (1,6,1):
	for col in my_range (1,7,1):
		
		if (fil == 1):
	       
			for col in my_range (1,dia_semana -1,1):
				print " ",
			for col in my_range (dia_semana,7,1):
				print cont,
				cont = cont + 1
			
		else:	
			if cont <= tope:
				print cont,
				cont = cont + 1
			
	print " "
