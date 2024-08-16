cantidad = -1
while cantidad <1 or cantidad>5:  
  try:
    cantidad = int(input('Cantidad de veces:'))
  except ValueError:
    print('dato incorrecto')

for i in range(cantidad):
  numero = -1
  while numero <1 or numero>1000:  
    try:
      numero = int(input('numero:'))
    except ValueError:
      print('dato incorrecto')

  if numero % 2==0:
    print('Es par')
  else:
    print('Es impar')
