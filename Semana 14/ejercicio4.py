import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def clasificar_edad(edad):
  if edad<=18:
    return 'Joven'
  elif edad<=30:
    return 'Joven Adulto'
  elif edad<=50:
    return 'Adulto'
  elif edad<=70:
    return 'Adulto Mayor'
  else:
    return 'Anciano'

def clasificar_obesidad(imc):
  valor = 'Obeso Extremo'
  if imc<=18.5:
    valor = 'Bajo'
  elif imc<=24.9:
    valor = 'Medio Peso'
  elif imc<=29:
    valor = 'Sobrepeso'
  elif imc<=34.9:
    valor = 'Obeso bajo peso '
  elif imc<=39.9:
    valor = 'Obeso Moderado'
  elif imc<=49.9:
    valor = 'Obeso Mórbido'
  return valor

def graficar(df,columna,titulo):
  cantidad = df[columna].value_counts()
  cantidad.plot(kind='pie',title=titulo,autopct='%1.1f%%')
  plt.show()
  print()

def estadisticas(df):
  print(f'Peso máximo {df["Peso"].max():.2f}')
  print(f'Peso mínimo {df["Peso"].min():.2f}')
  print(f'Peso promedio {df["Peso"].mean():.2f}')

def generar(cantidad):
  datos = np.empty((cantidad,7),dtype=object)
  for i in range(cantidad):
    decimal = np.random.rand()
    edad = np.random.randint(0,200)
    altura = np.random.randint(1,3)*decimal
    peso = np.random.randint(1,200)*decimal
    sexo = np.random.choice(['Hombre','Mujer'])
    imc = peso/(altura**2)
    clasificacion_edad = clasificar_edad(edad)
    clasificar_imc = clasificar_obesidad(imc)
    
    datos[i] = [edad,altura,peso,sexo,imc,clasificacion_edad,clasificar_imc]
  #convertir a pandas
  columnas = ['Edad','Altura','Peso','Sexo','IMC','Clasificación Edad','Clasificación IMC']
  df = pd.DataFrame(datos,columns=columnas)
  
  graficar(df,'Clasificación Edad','Clasificación por Edad')
  graficar(df,'Clasificación IMC','Clasificación por IMC')

  print(df)
  estadisticas(df)
    
n = 10
generar(n)
