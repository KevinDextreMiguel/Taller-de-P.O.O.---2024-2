class Computadora():#base
  __lista = []
  def __init__(self, precio_base, procesador, pantalla):
    self.__precio_base = precio_base
    self.__procesador = procesador
    self.__pantalla = pantalla
    self.__precio_final = 0
  #get
  def set_precio_base(self, precio_base):
    self.__precio_base = precio
  def set_procesador(self, procesador):
    self.__procesador = procesador
  def set_pantalla(self, pantalla):
    self.__pantalla = pantalla
  def set_precio_final(self, precio_final):
    self.__precio_final = precio_final
  #get
  def get_precio_base(self):
    return self.__precio_base
  def get_procesador(self):
    return self.__procesador
  def get_pantalla(self):
    return self.__pantalla
  def get_precio_final(self):
    return self.__precio_final
  #str
  def __str__(self):
    return f'Precio final: {self.__precio_final}, procesador: {self.__procesador}, pantalla: {self.__pantalla}'
  #agregar
  def agregar(self, obj):
    self.__lista.append(obj)
  def listar(self):
    for obj in self.__lista:
      print(obj)


class Laptop(Computadora):#derivada
  def __init__(self, precio_base, procesador, pantalla):
    super().__init__(precio_base, procesador, pantalla)

  def precio_pantalla(self):
    if self.get_pantalla() == 'tactil':
      self.set_precio_final(self.get_precio_base()*1.05)
  def precio_final(self):
    self.precio_pantalla()
    #procesador
    if self.get_procesador() == 'i5':
      self.set_precio_final(self.get_precio_base()*0.1+self.get_precio_final())
    elif self.get_procesador() == 'i7':
      self.set_precio_final(self.get_precio_base()*0.15+self.get_precio_final())
        

class Desktop(Computadora):#derivada
  def precio_pantalla(self):
    if self.get_pantalla() == 'HD':
      self.set_precio_final(200)
    else:
      self.set_precio_final(300)
  def precio_final(self):
    #procesador
    self.precio_pantalla()
    if self.get_procesador() == 'i5':
      self.set_precio_final(self.get_precio_base()*1.08+self.get_precio_final())
    elif self.get_procesador() == 'i7':
      self.set_precio_final(self.get_precio_base()*1.12+self.get_precio_final())
 


obj_laptop = Laptop(1000,'i3','tactil')
obj_laptop.agregar(obj_laptop)
obj_laptop.precio_final()

obj_desktop = Desktop(600,'i5','4k')
obj_desktop.agregar(obj_desktop)
obj_desktop.precio_final()

obj_laptop.listar()
