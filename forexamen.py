for fil in xrange (1, 5, 1):
  for col in xrange (1, 4, 1):
    if (fil==1):
      if (col==2):
        print "A",
      if (col==3):
        print "B",
      if (col==4):
        print "C",
      else:
        print "-"
    else:
      if (col==1):
        print fil -1,
      else:
        if (fil==3 and col==3) or (fil==4 and fil==2):
          print "*"
    print ""
