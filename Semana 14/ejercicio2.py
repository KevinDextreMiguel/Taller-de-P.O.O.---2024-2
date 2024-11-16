import pandas as pd
import matplotlib.pyplot as plt

def graficar(ventas,tipo):
  titulo = 'Ventas primer trimestre'
  graficos = {'lineas':'line','barras':'bar','circular':'pie','area':'area'}

  if tipo == 'circular':
    ventas.plot(kind=graficos[tipo],labels=ventas.index,autopct='%1.1f%%')
  else:
    fig,ax = plt.subplots()
    ventas.plot(kind=graficos[tipo])
    ax.set_ylabel('Nùmero de Ventas')
    ax.set_xlabel('Año')
    
  plt.title(titulo)
  plt.show()
  print()

ventas = [6578,6547,9876,5678]
anios = [2021,2022,2023,2024]
df_ventas = pd.Series(ventas,index=anios)
graficar(df_ventas,'circular')
graficar(df_ventas,'area')
graficar(df_ventas,'barras')
graficar(df_ventas,'lineas')
