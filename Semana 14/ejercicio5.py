import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def leer():
  url = 'https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv'
  df = pd.read_csv(url)
  return df

def hallar_precio_mayor(df):
  fila_precio_mayor = df.loc[df['Price'].idxmax()]
  fabricante = fila_precio_mayor['Manufacturer']
  modelo = fila_precio_mayor['Model']
  tipo = fila_precio_mayor['Type']
  precio = fila_precio_mayor['Price']
  
  print(f'Fabricante: {fabricante}')
  print(f'Modelo: {modelo}')
  print(f'Tipo: {tipo}')
  print(f'Precio Mayor: {precio}')

def intercambiar_fila(df):
  df.iloc[[0,1]] = df.iloc[[1,0]].values
  #df.to_excel('modificado.xlsx')

def graficar(df):
  precios_promedios = df.groupby(['Manufacturer','Model'])['Price'].mean()
  plt.figure(figsize=(16,26))
  precios_promedios.plot(kind='barh',color='red')
  plt.title'Precio Promedio por Modelo y Marca'
  plt.xlabel('Precio Promedio')
  plt.show()


df = leer()
#df.to_excel('datos.xlsx')
hallar_precio_mayor(df)
intercambiar_fila(df)
graficar(df)
