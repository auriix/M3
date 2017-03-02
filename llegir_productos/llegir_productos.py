# !/usr/bin/python
# -*-coding: utf-8-*-
##############################################
#          Llegim la taula "clientes"        #
##############################################

import os
import sys
import string
import psycopg2    # CAl fer "dnf -y install python-psycopg2"


##############################################
#          Ens connectem a la BBDD           #
##############################################
try:
	conn = psycopg2.connect(database="training", user="postgres", password="jupiter")
	print "DATABASE OPENED SUCCESSFULLY \n"
	
except:
	print "CONNECTION ERROR"
	exit(2)



##############################################
#            Declarem el cursor              #
##############################################
cur = conn.cursor()

os.system('clear')
sortir = False

##############################################
#              Menu principal                #
##############################################
while sortir == False:	
	
	os.system('clear')
	print "OPCIONS \n 1- Llegir taula 'productos': \n 0- Sortir \n"

	opcio = raw_input('Escull una opció [0-1]: ')
	
    # Comprovem si l'opció és correcta
	if not opcio.isdigit() or not ( int(opcio) >= 0 and int(opcio) <= 1 ):
		os.system('clear')
		print "Opció incorrecta, torna a provar \n"
		tecla = raw_input('Prem una tecla per continuar')

	else:
		opcio = int(opcio)

    # Sortim
	if opcio == 0:
		print "Adeu! \n"
		sortir = True

	# Llegim la taula "clientes"
	elif opcio == 1: 
		
		try:			
				cur.execute("SELECT * FROM productos");
				rows = cur.fetchall()
				
				
				os.system('clear')
				
				colnames = [desc[0] for desc in cur.description]
				print colnames

				
				#print " id_fab | id_producto |    descripcion    | precio  | existencias "

				for row in rows:
				   #print row[0],row[1],row[2],row[3]
				   print(" {:^10} {:^10} {:^18} {:^10} {:^10}".format(row[0], row[1], row[2], row[3], row[4]))
				
				tecla = raw_input('Prem una tecla per continuar')
		
		except psycopg2.Error as er :
			print "-------- ERROR:", er.pgcode, " -------- \n"
			conn.rollback()

##############################################
#        Ens desconnectem de la BBDD         #
##############################################
conn.close()
