import pandas as pd
import matplotlib.pyplot as plt

def generar_datos():
  dato = {'Meses':['Ene','Feb','Mar','Abr'],
          'Ventas':[6578,8765,9876,9854],
          'Gastos':[4567,4398,5456,6578]}
  dato = pd.DataFrame(dato)
  return dato

def graficar(datos):
  titulo = 'Evolución de ingresos y gastos'
  fig,ax = plt.subplots()
  plt.title(titulo)
  datos.plot(kind='line',x='Meses',y='Ventas',ax=ax,color='yellow')
  datos.plot(kind='line',x='Meses',y='Gastos',color='red',ax=ax)
  plt.grid(True)
  plt.show()

dato = generar_datos()
graficar(dato)
