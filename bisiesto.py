anyo = int(raw_input('Dame un a�o: '))

if anyo % 4 == 0  and  (anyo % 100 != 0  or  anyo % 400 == 0):
  print 'El a�o %d es bisiesto.' % anyo
else:
  print 'El a�o %d no es bisiesto.' % anyo
