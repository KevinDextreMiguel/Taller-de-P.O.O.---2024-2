import numpy as np

def generar_matriz():
  matriz = np.zeros((7,7))
  return matriz
def imprimir_matriz():
  print('============')
  print(matriz)
def cuartacolumna():
  matriz[:,3] = 0.5
  matriz[6,3] = 0.7
def _3ultimas_columnas():
  matriz[:,4:] = 1
def promedio_ultima_fila():
  promedio = np.mean(matriz[6,:])
  print(f'Proemdio última fila:{promedio}')

matriz = generar_matriz()
imprimir_matriz()
cuartacolumna()
imprimir_matriz()
_3ultimas_columnas()
imprimir_matriz()
promedio_ultima_fila()
