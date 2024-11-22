import pandas as pd
import numpy as np

class Data:
  def __init__(self):
    self.__df = None
    self.__copia = None
  def leer(self):
    self.__df = pd.read_csv('iris.csv',index_col=0)
    print(self.__df)
  def poner_nombre_columnas(self):
    nombres = ['sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species']
    self.__df.columns = nombres
    print(self.__df)
  def extraer_sexta_columna(self):
    specie = self.__df['species']
    print(specie)
  def estadistica(self):
    media = self.__df['sepallength'].mean()
    mediana = self.__df['sepallength'].median()
    desviacion_estandar = self.__df['sepallength'].std()
    print(f"Media columna sepallength: {media}")
    print(f"Mediana columna sepallength: {mediana}")
    print(f"Desviación estándar columna sepallength: {desviacion_estandar}")
  def insertar_nan(self):
    cantidad = 30
    self.__copia = self.__df.copy()
    indices_nan = np.random.choice(self.__copia.index, size=cantidad, replace=False)
    columnas_nan = np.random.choice(self.__copia.columns, size=cantidad,replace=True)
    for i in range(cantidad):
      self.__copia.loc[indices_nan[i],columnas_nan[i]] = np.nan
    print(self.__copia)
  def nan_segunda_columna(self):
    nan_valores = self.__copia['sepalwidth'].isna()
    cantidad_nan = nan_valores.sum()
    posiciones_nan = self.__copia[nan_valores].index.tolist()
    print(f"Cantidad de valores nan en la segunda columna: {cantidad_nan}")
    print(f"Posiciones de los valores nan en la segunda columna: {posiciones_nan}")
  def filas_sin_nan(self):
    filas_sin_nan = self.__copia.dropna()
    print(filas_sin_nan)
  def filtrar_condicion(self):
    filtra = self.__df[(self.__df['sepallength'] < 5) & (self.__df['petallength'] > 1.5)]
    print('filtrar')
    print(filtra)

objeto = Data()
objeto.leer()
objeto.poner_nombre_columnas()
objeto.extraer_sexta_columna()
objeto.estadistica()
objeto.insertar_nan()
objeto.nan_segunda_columna()
objeto.filas_sin_nan()
objeto.filtrar_condicion()
