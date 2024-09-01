def ingresar_n():
  n = -1
  while n<2 or n>9:
    try:
      n = int(input('Ingrese un número entre 2 y 9: '))
    except:
      print('Error')
  return n

def dibujar(n):
  for i in range(n):#filas
    print(end='  '*(n-i))#espacio
    #for espacio in range(n-i):
      #print(end='  ')
    for j in range(i+1):#columna
      print(end=' *')
    print()

def main():
  cont = 0
  cadena = 'S'
  while cadena == 'S' or cadena == 's':
    n = ingresar_n()
    dibujar(n)
    cadena = input('¿Desea continuar? (S/N): ')
    cont +=1
  print(f'Se han realizado {cont} dibujos')


main()
