import numpy as np

def generar():
  lista= [[-44, 12], [12.0, 51], [1300, -5.0]] 
  matriz = np.array(lista)
  return matriz
def imprimir(matriz):
  print('==================')
  print(matriz)
def restar_fila2(matriz):
  matriz[1] -= 5
def multiplicar_todo(matriz):
  matriz *= 2
def dividir_2primeras_filas(matriz):
  matriz[:2] /= -5
def imprimir_ultima_fila(matriz):
  filas,columnas = matriz.shape
  print(f'última fila: {matriz[filas-1]}')
def sumar_todo(matriz):
  suma = np.sum(matriz)
  print(f'Suma de elementos: {suma}')
def promedio_dos_primeras_filas(matriz):
  promedio = np.mean(matriz[:2])
  print(f'Promedio de dos primeras filas: {promedio}')

matriz = generar()
imprimir(matriz)
restar_fila2(matriz)
imprimir(matriz)
multiplicar_todo(matriz)
imprimir(matriz)
dividir_2primeras_filas(matriz)
imprimir(matriz)
imprimir_ultima_fila(matriz)
sumar_todo(matriz)
promedio_dos_primeras_filas(matriz)
