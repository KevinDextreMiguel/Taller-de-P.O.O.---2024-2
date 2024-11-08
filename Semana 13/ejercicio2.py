import pandas as pd
import matplotlib.pyplot as plt

def leer():
  df_titanic = pd.read_csv('titanic.csv',sep=';',decimal=',',encoding='latin-1',index_col=0)
  return df_titanic

def grafico_pie(df):
  lista = ['Fallecidos','Sobrevivientes']
  df.Survived.value_counts().plot.pie(autopct='%1.1f%%',labels=lista)
  plt.show()
  print()

def histograma(df):
  df_age= df.dropna(subset=['Age'])
  plt.figure(figsize=(10,5))
  plt.hist(df_age['Age'],bins=30,color='yellow',edgecolor='black')
  plt.xlabel('Edad')
  plt.ylabel('Frecuencia')
  plt.title('Histograma de edades')
  plt.show()
  print()

def grafico_barras_por_clase(df):
  df.Pclass.value_counts().plot.bar(color='red',edgecolor='blue')
  plt.xlabel('Clase')
  plt.ylabel('Frecuencia')
  plt.title('Frecuencia de pasajeros por clase')
  plt.show()
  print()

def grafico_barras_sobrevivientes_fallidos(df):
  df.groupby(['Pclass','Survived']).size().unstack().plot(kind='bar',
    title='Nùmero de personas que sobrevivieron por clase')
  

df = leer()
grafico_pie(df)
histograma(df)
grafico_barras_por_clase(df)
grafico_barras_sobrevivientes_fallidos(df)
