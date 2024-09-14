class Ticket:
  def __init__(self,precio,hora):
    self.__precio = precio
    self.__hora = hora
  
  def __str__(self):
    return f'{self.__precio} - {self.__hora}'
  
  def esNocheHora(self):
    return self.__hora[:2] >= '18'

  def  totalDescuento(self,n):
    if n > 4 and n < 10:
      return self.__precio * 0.9 * n
    elif n > 9:
      return self.__precio * 0.8 * n
    else:
      return self.__precio * n

  #set
  def set_precio(self,precio):
    self.__precio = precio
  def set_hora(self,hora):
    self.__hora = hora
  #get
  def get_precio(self):
    return self.__precio
  def get_hora(self):
    return self.__hora


objeto1 = Ticket(100,'18:30')
print(objeto1)
print(objeto1.esNocheHora())
print(objeto1.totalDescuento(5))

objeto2 = Ticket(200,'08:30')
print(objeto2)
print(objeto2.esNocheHora())
print(objeto2.totalDescuento(2))
