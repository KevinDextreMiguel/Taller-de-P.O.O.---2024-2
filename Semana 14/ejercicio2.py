import pandas as pd
import matplotlib.pyplot as plt

class Ventas:
  def __init__(self,dato):
    self.__dato = dato
    self.__titulo = 'Evolución de ventas'
    self.__graficos = {'lineas':'line','barras':'bar','area':'area','pie':'pie'}
  
  def graficar(self,tipo):
    if tipo == 'pie':
      self.__dato.plot(kind=self.__graficos[tipo],autopct='%1.1f%%')
    else:
      fig,ax = plt.subplots()
      self.__dato.plot(kind=self.__graficos[tipo])
      ax.set_ylabel('Ventas')
      ax.set_xlabel('Años')
      ax.set_title(self.__titulo)
    plt.show()
    print()
    

anios = [2021,2022,2023,2024]
ventas = [8976,8754,9871,7896]
df = pd.Series(ventas,index=anios)

objeto = Ventas(df)
objeto.graficar('pie')
objeto.graficar('barras')
objeto.graficar('area')
objeto.graficar('lineas')
