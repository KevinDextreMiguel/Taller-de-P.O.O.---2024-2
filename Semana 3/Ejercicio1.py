def ingresar_cadena():
  cadena = ''
  while len(cadena) != 10:
      cadena = input('Ingrese código generado: ')
  return cadena

def separar(cadena):
  TTTT = cadena[:4]
  HH = int(cadena[4:6])
  MM = int(cadena[6:8])
  SS = int(cadena[8:10])

  print(f'Código del trabajador: {TTTT}')
  print(f'Hora de entrada: {HH}')
  print(f'Minuto de entrada: {MM}')
  print(f'Segundos de entrada: {SS}')

cadena = ingresar_cadena() 
separar(cadena)
