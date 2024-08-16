codigo = int(input('Ingrese el còdigo: '))
cantidad = int(input('Ingrese el cantidad: '))

codigo = codigo % 10 
precio = 0

match codigo:
  case 1: precio = 15.75
  case 2: precio = 21
  case 3: precio = 8.5
  case 4: precio = 25
  case 5: precio = 13.25
  case _:print('Còdigo no vàlido')

if codigo>0 and codigo<6:
  print('Total a pagar s/',cantidad*precio,'.00')
