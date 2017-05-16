#coding:utf-8
import calendar

mes = input ("Inserta el mes (1-12): ") 
any = input ("Inserta el año (AAAA): ")
cont=1


num_dias_mes = calendar.monthrange(any, mes)[1]
dia_semana = calendar.weekday(any, mes, 1)

limite = num_dias_mes

print "lu ma mi ju vi sa do"
print "--------------------"

def my_range(inici, fi, increment):
    while inici <= fi:
        #Retorna l'element actual del rang (llista)
        yield inici
        inici = inici + increment

for fil in my_range (1, 1, 1):
	for col in my_range (1, dia_semana -1 ,1):
		print " ",
	for col in my_range (dia_semana, 7, 1):
		print cont,
		cont = cont + 1
	print " "
	
for fil in my_range (1,5,1):
	for col in my_range (1,7,1):
		if cont <= limite:
			print cont,
			cont = cont + 1
		else:
			print " ",
	
	print " "
