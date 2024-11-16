import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Encuesta:
  def __init__(self,n):
    self.__edad = 0
    self.__altura = 0
    self.__peso = 0
    self.__imc = 0
    self.__sexo = ''
    self.__clasificacion_edades = ''
    self.__clasificacion_imc = ''
    self.__tamanio = n
    self.__datos = np.empty((self.__tamanio,7),dtype=object)
  def calcula_imc(self):
    self.__imc = self.__peso / (self.__altura**2)
  def clasificar_edad(self):
    if self.__edad <= 18:
      self.__clasificacion_edades = 'Joven'
    elif self.__edad <= 30:
      self.__clasificacion_edades = 'Joven Adulto'
    elif self.__edad <= 50:
      self.__clasificacion_edades = 'Adulto'
    elif self.__edad <= 70:
      self.__clasificacion_edades = 'Adulto Mayor'
    else:
      self.__clasificacion_edades = 'Anciano'
  def clasificar_imc(self):
    if self.__imc <= 18.5:
      self.__clasificacion_imc = 'Bajo'
    elif self.__imc <= 24.9:
      self.__clasificacion_imc = 'Medio Peso'
    elif self.__imc <= 29:
      self.__clasificacion_imc = 'Sobre Peso'
    elif self.__imc <= 34.9:
      self.__clasificacion_imc = 'Obeso bajo peso'
    elif self.__imc <= 39.9:
      self.__clasificacion_imc = 'Obeso Moderado'
    elif self.__imc <= 49.9:
      self.__clasificacion_imc = 'Obeso Mórbido'
    else:
      self.__clasificacion_imc = 'Obeso Extremo'
  def generar(self):
    for i in range(self.__tamanio):
      self.__edad = np.random.randint(0,300)
      self.__altura = np.random.randint(100,200)/100
      self.__peso = np.random.randint(1,200)
      self.__sexo = np.random.choice(['M','F'])
      self.calcula_imc()
      self.clasificar_edad()
      self.clasificar_imc()

      self.__datos[i] = [self.__edad,self.__altura,self.__peso,self.__imc,self.__sexo,self.__clasificacion_edades,self.__clasificacion_imc]
    
    columnas = ['Edad','Altura','Peso','IMC','Sexo','Clasificación de edad','Clasificación de IMC']
    df = pd.DataFrame(self.__datos,columns=columnas)
    print(df)
    self.graficar(df,'Clasificación de edad','Gràfico')
    self.graficar(df,'Clasificación de IMC','Gràfico')
    self.estadistica(df,'Peso')

  def graficar(selfdf,df,columna,titulo):
    cantidad = df[columna].value_counts()
    cantidad.plot(kind='pie',autopct='%1.1f%%')
    plt.title(titulo)
    plt.show()
    print()
  
  def estadistica(self,df,columna):
    print(f'Peso promedio: {df[columna].mean()}')
    print(f'Peso mínimo: {df[columna].min()}')
    print(f'Peso máximo: {df[columna].max()}')


n = int(input('N: '))
objeto = Encuesta(n)
objeto.generar()
