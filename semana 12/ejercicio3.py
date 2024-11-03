import pandas as pd
import numpy as np

def leer():
  df = pd.read_csv('bupa.csv',header=None)
  return df

def imprimir(dato):
  print('============================')
  print(dato)

def dar_nombres_columnas():
  lista = ['mcv', 'alkphos', 'sgpt', 'sgot', 'gammagt', 'drinks','selector' ]
  df.columns = lista

def calcular():
  media = df['alkphos'].mean()
  mediana = df['alkphos'].median()
  moda = df['alkphos'].mode()
  print('media de alkphos: ',media)
  print('mediana de alkphos: ',mediana)
  print('moda de alkphos: ',moda)

def nan_aleatoria():
  copia = df.copy()
  nan = np.random.choice(copia.index,size=50,replace=False)
  copia.loc[nan] = np.nan
  return copia
def contar_nan(copia):
  cantidad = copia.isna().sum()
  print('Cantidad de Nan: ',cantidad)

def eliminar_nan(copia):
  copia = copia.dropna()
  return copia

df = leer()
imprimir(df)
dar_nombres_columnas()
imprimir(df)
calcular()
copia = nan_aleatoria()
imprimir(copia)
contar_nan(copia)
copia = eliminar_nan(copia)
imprimir(copia)
