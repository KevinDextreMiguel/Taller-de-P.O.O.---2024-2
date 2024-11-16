import pandas as pd
import matplotlib.pyplot as plt

class Ventas:
  def __init__(self,datos,titulo):
    self.__datos = datos
    self.__titulo = titulo
  
  def graficar(self):
    self.__datos.plot(kind='pie',title=titulo,autopct='%1.1f%%')
    plt.savefig(titulo+'.png')
    plt.show()

datos = {'Enero':1200,'Febrero':1400,'Marzo':1600}
ventas = pd.Series(datos)
titulo = 'Ventas'
#creamos un objeto
objeto_ventas = Ventas(ventas,titulo)
objeto_ventas.graficar()
