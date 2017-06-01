#coding: utf8
#Definim la funció my_range.
def my_range(inici, fi, increment):
    while inici <= fi:
        #Retorna l'element actual del rang (llista)
        yield inici
        inici = inici + increment

# - A B C
# 1 
# 2
# 3
# 4

for fil in my_range(1,5,1):
  for col in my_range(1,4,1):
    if (fil==1):
      if (col==2):
        print "A"
      if (col==3):
        print "B"
      if (col==4):
        print "C"
      
      else:
        print "-"
    else:
      if (col==1):
        print fil-1
        
       
