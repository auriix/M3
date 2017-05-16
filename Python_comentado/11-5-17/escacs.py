def my_range(inici, fi, increment):
    while inici <= fi:
        #Retorna l'element actual del rang (llista)
        yield inici
        inici = inici + increment


for fil in my_range (1,8,1):
	for col in my_range (1,8,1):
		if (fil%2==col%2):
			print "N",
			
		else:
			print "B",
	
	print ""
