import pandas as pd

class Volumen():#base
  def __init__(self,numero,nombre):
    self.__numero = numero
    self.__nombre = nombre
  def get_numero(self):
    return self.__numero
  def get_nombre(self):
    return self.__nombre
  def set_numero(self,numero):
    self.__numero = numero
  def set_nombre(self,nombre):
    self.__nombre = nombre
  def __str__(self):
    return f'numero: {self.__numero}, nombre: {self.__nombre}'
  

class Libro(Volumen):
  def __init__(self,numero,nombre,id):
    super().__init__(numero,nombre)
    self.__id = id
  def get_id(self):
    return self.__id
  def set_id(self,id):
    self.__id = id
  

class Periodico(Volumen):
  def __init__(self,numero,nombre,id):
    super().__init__(numero,nombre)
    self.__id = id
  def get_id(self):
    return self.__id
  def set_id(self,id):
    self.__id = id


class Biblioteca():
  def __init__(self,nombre,direccion):
    self.__nombre = nombre
    self.__direccion = direccion
    self.__lista = []
  def agregar(self,objeto):
    if self.existe_elemento(objeto):
      print('ya existe el elemento')
    else:
      self.__lista.append(objeto)
      print('añadido exitosamente')
  def existe_elemento(self,obj):
    for objeto in self.__lista:
      if objeto.get_numero() == obj.get_numero():
        return True
    return False
  def eliminar(self,posicion):
    if posicion >= 0 and posicion < len(self.__lista):
      self.__lista.pop(posicion)
    else:
      print('posicion invàlida')  
  def listar(self):
    for obj in self.__lista:
      print(obj)
  def guardar_excel(self):
    lista1 = []
    lista2 = []
    for obj in self.__lista:
      lista1.append(obj.get_numero())
      lista2.append(obj.get_nombre())
    df = pd.DataFrame({"id":lista1,"nombre":lista2})
    df.to_excel('dato.xlsx',sheet_name='ejercicio 2',index=False)

    pd.DataFrame()
  #get
  def get_nombre(self):
    return self.__nombre
  def set_nombre(self,nombre):
    self.__nombre = nombre
  #set
  def set_direccion(self,direccion):
    self.__direccion = direccion
  def get_direccion(self):
    return self.__direccion


obj_periodico = Periodico(1,'Trome',1)
obj_biblioteca = Biblioteca('biblioteca','direccion')
obj_biblioteca.agregar(obj_periodico)
obj_libro = Libro(2,'Las Adas',2)
obj_biblioteca.agregar(obj_libro)
obj_biblioteca.listar()
obj_biblioteca.guardar_excel()
