def ingresar_n():
  n=-1
  while n<0:
    try:
      n = int(input("Ingrese un numero: "))
    except ValueError:
      print('error')
    
  return n

def ingresar_b():
  b=-1
  while b<1 or b>5:
    try:
      b = float(input("B: "))
    except ValueError:
      print('error')
    
  return b


def sumatoria(n,b):
  suma = 0
  cont2 = 2
  denominador = 4
  for i in range(n):
    numerador = cont2 * b
    suma += numerador/denominador * (-1)**i
    #if i % 2 == 0:
    #  suma += numerador/denominador
    #else:
    #  suma -= numerador/denominador
    cont2 += 2
    denominador += 3
  
  print('suma: ',suma)


#main
n = ingresar_n()
b = ingresar_b()
sumatoria(n,b)
