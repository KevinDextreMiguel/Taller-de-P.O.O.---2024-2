import numpy as np

def generar():
  matriz = np.random.rand(5,3)
  #con valores especìfico
  #matriz = np.random.randint(100,1000,size=(5,3))#(inicial,final,dimensión)
  return matriz
def imprimir():
  print(matriz)
def imprimir_elementos_mayores():
  filas,columnas = matriz.shape#(5,5)
  print('\nElementos mayores que 0.5')
  for i in range(filas):
    for j in range(columnas):
      if matriz[i,j] > 0.5:
        print(f'[{i},{j}]:{matriz[i,j]}')

matriz = generar()
imprimir()
imprimir_elementos_mayores()
