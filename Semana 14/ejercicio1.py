import pandas as pd
import matplotlib.pyplot as plt

def graficar(ventas,titulo):
  ventas.plot(kind='pie',title=titulo,autopct='%1.1f%%')
  plt.savefig('grafico.png')
  plt.show()


dato = {'Enero':450,'Febrero':400,'Marzo':500}
titulo = 'Ventas primer trimestre'
ventas = pd.Series(dato)
graficar(ventas,titulo)
