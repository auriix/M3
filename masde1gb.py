#coding: utf-8
import os
import time

path_to_explore = raw_input("Escriu la ruta:")
tamanyo = 0
       
for root, dirs, files in os.walk(path_to_explore):
    for x in files:
        name_path = os.path.join (root, x)
        
#Mostrem el que ocupa de cada arxiu.
tamanyo = os.stat(name_path).st_size
        

if (tamanyo >= 2**30):
  print "Arxius que ocupen 1GB o mès:\n", name_path
