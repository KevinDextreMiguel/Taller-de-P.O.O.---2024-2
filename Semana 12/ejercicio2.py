import pandas as pd

def leer():
  df = pd.read_excel('colesteroles.xlsx')
  df = pd.DataFrame(df)
  return df

def imprimir(dato):
  print('============================')
  print(dato)
def agregar_fila(df):
  nueva_fila = {
      "nombre": "Carlos Rivas",
      "edad": 28,
      "sexo": "Hombre",
      "peso": 80,
      "altura": 1.78,
      "colesterol": 245
  }

  df.loc[len(df)] = nueva_fila
  return df

def utltimos_7registros():
  print('ùltimas 7 filas: ',df.tail(7))

def agregar_columna():
  lista = ["No", "No", "Si", "No", "Si", "No", "Si", "No", "Si", "No", "Si", 
    "No", "Si", "No","No"]
  df['Diabetes'] = lista

def crear_nuevo_archivo():
  nuevo = 'nuevo.xlsx'
  df.to_excel(nuevo,index=False)
  df_nuevo = pd.read_excel(nuevo)
  return df_nuevo


df = leer()
imprimir(df)
df = agregar_fila(df)
utltimos_7registros()
agregar_columna()
imprimir(df)
nuevo = crear_nuevo_archivo()
imprimir(nuevo)
