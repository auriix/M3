#coding:utf-8

def my_range(inici,fi,increment):
	while inici <= fi:
		yield inici
		inici = inici + increment


palo=["1","2","3","4"]
num=["1","2","3","4","5","6","7","8","9","10","11","12","13"]
cont= 52
from random import randint

for palo in my_range(1,4,1):
	for num in my_range(1,13,1):
  
		palo=randint(1,4)
		num=randint(1,13)
    
		if (num <= 10) :
			carta = num

		if (num == 11) :
			carta = "J"

		if (num == 12) :
			carta = "Q"

		if (num == 13) :
			carta = "K"
			
		if(palo == 1):
			palo= "D"
			
		if(palo == 2):
			palo= "C"
			
		if(palo == 3):
			palo= "T"
		
		if(palo == 4):
			palo= "P"
				
		print num, palo
		
cont= cont- 1
