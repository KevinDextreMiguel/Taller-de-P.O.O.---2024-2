class Administrador:
  def __init__(self,id,nombre):
    self.__id = id
    self.__nombre = nombre
  def __str__(self):
    return f"Id: {self.__id} Nombre: {self.__nombre}"


class Propietario:
  def __init__(self,id,nombre):
    self.__id = id
    self.__nombre = nombre
  def __str__(self):
    return f"Id: {self.__id} Nombre: {self.__nombre}"

class JuntaPropietarios:
  def __init__(self,id,fecha_creacion):
    self.__id = id
    self.__fecha_creacion = fecha_creacion
    self.__propietarios = []
  def agregar_propietario(self,objeto_propietario):
    self.__propietarios.append(objeto_propietario)
  def obtener_info(self):
    print(f"Id: {self.__id} Fecha de creacion: {self.__fecha_creacion}")
    print("Propietarios:")
    for propietario in self.__propietarios:
      print(propietario)#==============

class Departamento:
  def __init__(self,id,numero_habitacion):
    self.__id = id
    self.__numero_habitacion = numero_habitacion
  def __str__(self):
    return f"Id: {self.__id} Numero de habitacion: {self.__numero_habitacion}"

class Edificio:
  def __init__(self,id,direccion):
    self.__id = id
    self.__direccion = direccion
    self.__departamentos = []
    self.__administrador = None
    self.__junta_propietarios = None
  def agregar_departamento(self,objeto_departamento):
    self.__departamentos.append(objeto_departamento)
  def asignar_administrador(self,objeto_administrador):
    self.__administrador = administrador
  def asignar_junta_propietarios(self,objeto_junta_propietarios):
    self.__junta_propietarios = junta_propietarios
  def obtener_info(self):
    print(f"Id: {self.__id} Direccion: {self.__direccion}")
    print("Departamentos:")
    for departamento in self.__departamentos:
      print(departamento)
    print('Información del administrador')
    print(self.__administrador)
    print('junta_propietarios')
    self.__junta_propietarios.obtener_info()



administrador = Administrador(1,"Juan")

propietario1 = Propietario(1,"Maria")
propietario2 = Propietario(2,"Pedro")
propietario3 = Propietario(3,"Ana")

junta_propietarios = JuntaPropietarios(1,"2024-11-23")
junta_propietarios.agregar_propietario(propietario1)
junta_propietarios.agregar_propietario(propietario2)
#junta_propietarios.agregar_propietario(propietario3)

departamento1 = Departamento(1,6)
departamento2 = Departamento(2,3)
departamento3 = Departamento(3,8)

edificio = Edificio(1,"Av. Siempre Viva 123")
edificio.agregar_departamento(departamento1)
edificio.agregar_departamento(departamento2)
edificio.agregar_departamento(departamento3)
edificio.asignar_administrador(administrador)
edificio.asignar_junta_propietarios(junta_propietarios)

edificio.obtener_info()
