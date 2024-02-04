from math import ceil

grados = float(input('Dame un angulo (en grados):'))

cuadrante = int(ceil(grados) % 360) / 90
if cuadrante == 0:
 print ('primer cuadrante')
 if cuadrante == 1:
   print ('segundo cuadrante')
if cuadrante == 2:
  print('tercer cuadrante')
if cuadrante == 3:
  print('cuarto cuadrante')