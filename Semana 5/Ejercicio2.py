class CuentaBancaria:
  #constructor
  def __init__(self,nombre,cantidad,tasaInteres):
    self.__nombre = nombre
    self.__cantidad = cantidad
    self.__tasaInteres = tasaInteres


  def aplica_interes(self):
    self.__cantidad += self.__cantidad * self.__tasaInteres

  def imprimir(self):
    print('==============================')
    print(f'Nombre: {self.__nombre}')
    print(f'Cantidad: {self.__cantidad}')
    print(f'Tasa de interés: {self.__tasaInteres*100}%')

  #set
  def set_nombre(self,nombre):
    self.__nombre = nombre
  def set_cantidad(self,cantidad):
    self.__cantidad = cantidad
  def set_tasaInteres(self,tasaInteres):
    self.__tasaInteres = tasaInteres

  #get
  def get_nombre(self):
    return self.__nombre
  def get_cantidad(self):
    return self.__cantidad
  def get_tasaInteres(self):
    return self.__tasaInteres


objeto1 = CuentaBancaria('Valia',1000,0.03)
objeto1.aplica_interes()
objeto1.imprimir()
objeto1.set_tasaInteres(0.02)
objeto1.aplica_interes()
objeto1.imprimir()
