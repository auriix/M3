def my_range(inici, fi, increment):
    while inici <= fi:
        #Retorna l'element actual del rang (llista)
        yield inici
        inici = inici + increment


for fil in my_range (1,4,1):
	for col in my_range (1,8,1):
		
		if (fil==1) or (fil==4) or (col==1) or (col==8):
			print "*",
				
		
		else:
			if (fil==2 and (col==4 or col==5)):
				print ".",
				
			elif (fil==3 and col==4):
				print "\\",
				
			elif (fil==3 and col==5):
				print "/",
				
			else:
				print " ",
	
				
	print " "
			
