class Computadora():#base (padre)
  __lista = list()
  def __init__(self, precio, procesador, pantalla):
    self.__precio = precio
    self.__procesador = procesador
    self.__pantalla = pantalla
    self.__precio_pantalla = 0
  def __str__(self):
    return f"Precio: {self.__precio}, Procesador: {self.__procesador}, Pantalla: {self.__pantalla}"
  def agregar(self,objeto):
    self.__lista.append(objeto)
  def mostrar(self):
    for objeto in self.__lista:
      print(objeto)
  #get
  def get_precio(self):
    return self.__precio
  def get_procesador(self):
    return self.__procesador
  def get_pantalla(self):
    return self.__pantalla
  def get_precio_pantalla(self):
    return self.__precio_pantalla
  #set
  def set_precio(self, precio):
    self.__precio = precio
  def set_procesador(self, procesador):
    self.__procesador = procesador
  def set_pantalla(self, pantalla):
    self.__pantalla = pantalla
  def set_precio_pantalla(self, precio_pantalla):
    self.__precio_pantalla = precio_pantalla

class Laptop(Computadora):#derivada
  def __init__(self, precio, procesador, pantalla):
    super().__init__(precio, procesador, pantalla)
  def precio_final(self):
    if self.get_pantalla() == 'tactil':
      self.set_precio_pantalla(self.get_precio() * 0.05)
    
    if self.get_procesador() == 'i5':
      self.set_precio(self.get_precio()*1.1)
    elif self.get_procesador() == 'i7':
      self.set_precio(self.get_precio()*1.15)
    self.set_precio(self.get_precio()+self.get_precio_pantalla())
    
class Desktop(Computadora):
  def __init__(self, precio, procesador, pantalla):
    super().__init__(precio, procesador, pantalla)
  def precio_final(self):
    if self.get_pantalla() == 'HD':
      self.set_precio_pantalla(200)
    else:
      self.set_precio_pantalla(300)
    
    if self.get_procesador() == 'i5':
      self.set_precio(self.get_precio()*1.08)
    elif self.get_procesador() == 'i7':
      self.set_precio(self.get_precio()*1.12)
    self.set_precio(self.get_precio()+self.get_precio_pantalla())


objeto_laptop = Laptop(1000,'i5','tactil')
objeto_laptop.precio_final()
objeto_laptop.agregar(objeto_laptop)
objeto_laptop.mostrar()
print('======================')
objeto_desktop = Desktop(600,'i7','HD')
objeto_desktop.precio_final()
objeto_desktop.agregar(objeto_desktop)
objeto_desktop.mostrar()
