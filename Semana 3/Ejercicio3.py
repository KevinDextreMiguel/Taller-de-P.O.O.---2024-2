def ingresar_n():
  n = -1
  while n<2 or n>9:
    try:
      n = int(input('Ingrese un número entre 2 y 9: '))
    except:
      print('Error')
  return n

def triangulo(letra,n):
  for j in range(n):#columna
    print(chr(letra),end=' ')
    letra +=1

def dibujar(n):
  letra = ord('A')
  for i in range(n):#filas
    triangulo(letra,n-i)
    print(end='  '*i*2)#espacio
    triangulo(letra,n-i)
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
