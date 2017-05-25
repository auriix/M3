# coding: utf-8

# Imports
import os
import stat

path_to_explore = raw_input('Introduzca la ruta a explorar: ')


for root, dirs, files in os.walk(path_to_explore):
	for d in dirs:
		permisosd = oct(stat.S_IMODE (os.stat(path_to_explore).st_mode))
		
		if (permisosd[-1] != 0):
			print "Hi ha un error de seguretat."
		else:
			print "No hi han errors de seguretat."
			
	for f in files:
		permisosf = oct(stat.S_IMODE (os.stat(path_to_explore).st_mode))
		 
		if (permisosf[-1] != 0):
			print "Hi ha un error de seguretat."
		else:
			print "No hi han errors de seguretat."
