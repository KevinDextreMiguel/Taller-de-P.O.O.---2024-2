class Articulo:
  def __init__(self,nombre,precio):
    self.__nombre = nombre
    self.__precio = precio

  def __str__(self):
    return f'{self.__nombre} - {self.__precio}'

  #get
  def get_nombre(self):
    return self.__nombre
  def get_precio(self):
    return self.__precio
  #set
  def set_nombre(self,nombre):
    self.__nombre = nombre
  def set_precio(self,precio):
    self.__precio = precio


objeto_articulo1 = Articulo('Artículo a',10.67)
print(objeto_articulo1)

nombre = input('Ingrese el nombre del artículo: ')
precio = float(input('Ingrese el precio del artículo: '))
objeto_articulo2 = Articulo(nombre,precio)
print(objeto_articulo2)
