
fil=0
col=0

def my_range(inici, fi, increment):
    while inici <= fi:
        #Retorna l'element actual del rang (llista)
        yield inici
        inici = inici + increment


for fil in my_range (1,5,1):
	print ""
	for col in my_range (1,4,1):
		if (fil==1):
			if (col==1):
				print "-",
			if (col==2):
				print "A",
			if (col==3):
				print "B",
			if (col==4):
				print "C",
			
		else:
			if (col==1):
				print fil -1,
			else:
				if (fil==3 and col==2) or (fil==4 and col==3):
					print "*",
				else:
					print "-",
	
