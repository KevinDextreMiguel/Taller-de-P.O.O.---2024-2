import pandas as pd
import random

def generar_lista():
  lista = list()
  for _ in range(4):
    lista.append(random.randint(1000,9999))
  return lista

def generar_datos():
  datos = {
      'Mes':['Enero','Febrero','Marzo','Abril'],
      'Ventas':generar_lista(),#[30500,35600,28300,3345] -> lista
      'Gastos':generar_lista()
  }
  df = pd.DataFrame(datos)
  return df

def imprimir(df):
  print(df)


df = generar_datos()
imprimir(df)
