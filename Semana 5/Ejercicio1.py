import random

def insertar_columna(letra,numero_inicial,numero_final):
  lista = list()
  while len(lista) < 5:
    numero = random.randint(numero_inicial,numero_final)
    if numero not in lista:
      lista.append(numero)
  bingo[letra] = lista
  
def insertar():
  numero_final = 15
  for i in 'BINGO':
    insertar_columna(i,numero_final-14,numero_final)
    numero_final += 15
    
def mostrar():
  for clave,valor in bingo.items():
    print(clave,valor)
    


bingo = dict()
insertar()
mostrar()
