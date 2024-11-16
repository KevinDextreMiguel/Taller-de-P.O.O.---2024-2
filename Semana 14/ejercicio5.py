import pandas as pd
import matplotlib.pyplot as plt

class Data:
  def __init__(self):
    self.__df = ''
    self.__url = 'https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv'
  def leer(self):
    self.__df = pd.read_csv(self.__url)
  def hallar_mayor_precio(self):
    fila_mayor_precio = self.__df.loc[self.__df['Price'].idxmax()]
    fabricante = fila_mayor_precio['Manufacturer']
    modelo = fila_mayor_precio['Model']
    print(f'El fabricante con mayor precio es {fabricante} con el modelo {modelo}')
  def guardar(self):
    self.__df.to_excel('datos.xlsx',index=False)
    print('Se ha guardado el archivo')
  def intercambiar(self):
    self.__df.iloc[[0,1]] = self.__df.iloc[[1,0]]
    self.__df.to_excel('modificado.xlsx',index=False)
    print('Se hizo el cambio')
  def graficar(self):
    precios_proemdios = self.__df.groupby(['Manufacturer','Model'])['Price'].mean()
    plt.figure(figsize=(16,20))
    precios_proemdios.plot(kind='barh',color='green')
    plt.show()

objeto = Data()
objeto.leer()
objeto.guardar()
objeto.hallar_mayor_precio()
objeto.intercambiar()
objeto.graficar()
