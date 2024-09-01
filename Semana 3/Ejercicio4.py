import random

def ingresar_n():
  n = -1
  while n<1 or n>40:
    try:
      n = int(input('Ingrese n: '))
    except:
      print('Error')
  return n

def generar(lista,n):
  for i in range(n):
    numero = random.randint(1,9)
    lista.append(numero)


def imprimir(lista):
  for valor in lista:
    print(valor,end=' ')
  print()

def repeticiones(lista):
  conjunto = set(lista)
  for i in conjunto:
    print(f'El número {i} se repite {lista.count(i)}')

def reeplazar(lista):
  primos=[2,3,5,7]
  for i in range(len(lista)):
    if lista[i] in primos:
      lista[i] = lista[i] + 1


lista=[]
n = ingresar_n()
generar(lista,n)
imprimir(lista)
repeticiones(lista)
reeplazar(lista)
imprimir(lista)
