#coding:utf-8

#Lista con personajes de Mario.

personajes = ["mario","luigi"]
print personajes
print personajes [0]

for pj in personajes:
	print pj,

personajes.append ("princesspeach")
personajes.insert (0,"toad")
print ""
print personajes

print "Se ha añadido a la lista:", personajes[3], "y", personajes [0]


print "Se ha eliminado de la lista:", personajes[1]
personajes.remove ("mario")

for pj in personajes:
	print pj,
