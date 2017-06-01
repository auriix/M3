def my_range(inici, fi, increment):
    while inici <= fi:
        #Retorna l'element actual del rang (llista)
        yield inici
        inici = inici + increment


for fil in my_range (1,6,1):
	for col in my_range (1,5,1):
		
		if (fil==1 and col==3):
			print "*",
		else:	
			if (fil==4) or ((fil==2) and (col==3)) or ((fil==3) and (col==2 or col==3 or col==4)):
				print "A",
		
			
			elif ((fil==6 or fil==5) and (col==3)):
					print "N",
			else:
				print " ",
	
	print ""
