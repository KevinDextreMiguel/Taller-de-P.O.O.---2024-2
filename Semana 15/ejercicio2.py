import pandas as pd
import numpy as np

class Datos:
  def __init__(self):
    self.__df = None
    self.__copia = None
  def leer(self):
    self.__df = pd.read_csv('iris.csv',index_col=0)
    #print(self.__df)
  def poner_encabezados(self):
    names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species') 
    self.__df.columns = names
    print(self.__df)
  def extraer_6columna(self):
    columna = self.__df.species #self.__df['species']
    print('información columna species')
    print(columna)
  def estadistica(self):
    media = self.__df.sepallength.mean()
    mediana = self.__df['sepallength'].median()
    desviacion = self.__df.sepallength.std()
    print(f'media: {media}')
    print(f'mediana: {mediana}')
    print(f'desviacion: {desviacion}')
  def crear_copia(self):
    cantidad = 30
    self.__copia = self.__df.copy()
    indices_nan = np.random.choice(self.__copia.index, cantidad, replace=False)
    columnas_nan = np.random.choice(self.__copia.columns, cantidad, replace=True)
    for i in range(cantidad):
      self.__copia.loc[indices_nan[i], columnas_nan[i]] = np.nan
    print(self.__copia)
  def nan_segunda_columna(self):
    nan_sepalwidth = self.__copia['sepalwidth'].isna()
    cantidad = nan_sepalwidth.sum()
    indices = self.__copia[nan_sepalwidth].index.tolist()
    print(f'Cantidad de valores nan en la segunda columna: {cantidad}')
    print(f'Indices de los valores nan en la segunda columna: {indices}')
  def filas_sin_nan(self):
    filas_sin_nan = self.__copia.dropna()
    print(filas_sin_nan)
  def filtrar(self):
    data = self.__copia[(self.__copia['sepallength']<5.0) & (self.__copia['petallength']>1.5)]
    print('filtro')
    print(data)

    

objeto = Datos()
objeto.leer()
objeto.poner_encabezados()
objeto.extraer_6columna()
objeto.estadistica()
objeto.crear_copia()
objeto.nan_segunda_columna()
objeto.filas_sin_nan()
objeto.filtrar()
