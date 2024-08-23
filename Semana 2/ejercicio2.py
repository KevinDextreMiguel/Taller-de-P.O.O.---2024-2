def ingresar_nota():
  nota=-1
  while nota<0 or nota>10:
    try:
      nota = int(input("Ingrese una nota: "))
    except ValueError:
      print('error')
    
  return nota


def imprimir_nota(nota):
  mensaje = ''
  if nota > 8:
    mensaje = 'sobresaliente'
  elif nota > 6:
    mensaje = 'notable'
  elif nota == 6:
    mensaje = 'bien'
  elif nota == 5:
    mensaje = 'suficiente'
  else:
    mensaje = 'insuficiente'
  
  print(mensaje)


#main
nota = ingresar_nota()
imprimir_nota(nota)
