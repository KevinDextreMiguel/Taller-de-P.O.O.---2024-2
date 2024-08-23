def ingresar_n():
  n=-1
  while n<1 or n>120:
    try:
      n = int(input("Ingrese un numero: "))
    except ValueError:
      print('error')
    
  return n

def calcula_factorial(n):
  factorial = 1
  for i in range(1, n+1):
    factorial *= i
  return factorial


def sumatoria(n):
  e = 0
  dos = 2
  for i in range(1, n+1):
    numerador = i**2
    denominador = dos * calcula_factorial(i)
    e += numerador/denominador
  
  print('e: ',e)

n = ingresar_n()
sumatoria(n)
