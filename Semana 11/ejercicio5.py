import pandas as pd

def leer_dato():
  df = pd.read_csv('cotizacion.csv',sep=';',decimal=',',encoding='latin-1',index_col=0)
  return df

def imprimir(df):
  print(df)

def calcular(df):
  print('===========================')
  resultado = pd.DataFrame([df.min(),df.max(),df.mean()],
                  index=['Mínimo','Máximo','Promedio'])
  return resultado



df = leer_dato()
imprimir(df)
resultado = calcular(df)
imprimir(resultado)
