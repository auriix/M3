#! /usr/bin/python
# coding: utf-8

import os

path_to_explore="./d1/"

#Mostrar directoris

for root, dirs, files in os.walk(path_to_explore):
	for x in dirs:
		print x
		
print "------------------------------------------------"

#Mostrar arxius

for root, dirs, files in os.walk(path_to_explore):
	for x in files:
		print x
		
print "------------------------------------------------"

#Mostrar arxius i directoris

for root, dirs, files in os.walk(path_to_explore):
	for x in files:
		print x
		
	for x in dirs:
		print x
		
print "------------------------------------------------"

#Mostrar sol les rutes dels arxius

for root, dirs, files  in os.walk(path_to_explore):
	for x in files:
		
		name_path=os.path.join(root, x)
		print (name_path)
	
print "------------------------------------------------"

#Mostrar les rutes d'arxius i directoris

for root, dirs, files  in os.walk(path_to_explore):
	for x in dirs:
		
		name_path=os.path.join(root, x)
		print (name_path)
	
	for x in files:
		
		name_path=os.path.join(root, x)
		print (name_path)

print "------------------------------------------------"

#Mostrar les rutes d'arxius i el seu tamany en bytes.

for root, dirs, files  in os.walk(path_to_explore):
	for x in files:
		name_path=os.path.join(root, x)
		print (name_path)
		print os.path.getsize (name_path)
