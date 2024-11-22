class Administrador:
  def __init__(self,id,nombre):
    self.__id = id
    self.__nombre = nombre
  def __str__(self):
    return f"ID: {self.__id} Nombre: {self.__nombre}"

class Propietario:
  def __init__(self,id,nombre):
    self.__id = id
    self.__nombre = nombre
  def __str__(self):
    return f"ID: {self.__id} Nombre: {self.__nombre}"

class JuntaPropietarios:
  def __init__(self,id,fecha_creacion):
    self.__id = id
    self.__fecha_creacion = fecha_creacion
    self.__propietarios = []
  def agregar_propietario(self,propietario):
    self.__propietarios.append(propietario)
  def obtener_info(self):
    print(f"ID: {self.__id} Fecha de creacion: {self.__fecha_creacion}")
    print("Propietarios:")
    for propietario in self.__propietarios:
      print(propietario)

class Departamento:
  def __init__(self,id,numero_habitaciones):
    self.__id = id
    self.__numero_habitaciones = numero_habitaciones
  def __str__(self):
    return f"Id: {self.__id}, nùmero de habitaciones: {self.__numero_habitaciones}" 


class Edificio:
  def __init__(self,id,direccion):
    self.__id = id
    self.__direccion = direccion
    self.__departamentos = []
    self.__administrador = None
    self.__juntas_propietarios = None
  def agregar_departamento(self,departamento):
    self.__departamentos.append(departamento)
  def asignar_administrador(self,administrador):
    self.__administrador = administrador
  def asociar_junta_propietarios(self,junta_propietarios):
    self.__juntas_propietarios = junta_propietarios
  def obtener_info(self):
    print(f"ID: {self.__id} Dirección: {self.__direccion}")
    print("Departamentos:")
    for departamento in self.__departamentos:
      print(departamento)
    print('Administrador')
    print(self.__administrador)
    print('Juntas de propietarios')
    self.__juntas_propietarios.obtener_info()


#objeto administrativo
objeto_administrador = Administrador(1,"David Pèrez")

#objetos propiedtario
objeto_propietario1 = Propietario(1,"Juan Pérez")
objeto_propietario2 = Propietario(2,"María Gómez")
objeto_propietario3 = Propietario(3,"Ana Gómez")

#obejeto junta de propietarios 
objeto_junta_propietarios = JuntaPropietarios(1,"22/11/2024")
#agregar propietario a la junta
objeto_junta_propietarios.agregar_propietario(objeto_propietario1)
objeto_junta_propietarios.agregar_propietario(objeto_propietario2)

#crear un objeto departamento
objeto_departamento1 = Departamento(1,4)
objeto_departamento2 = Departamento(2,6)
objeto_departamento3 = Departamento(3,5)

#crear objeto edificio
objeto_edificio = Edificio(1,"Calle 123")
objeto_edificio.agregar_departamento(objeto_departamento1)
objeto_edificio.agregar_departamento(objeto_departamento2)
objeto_edificio.agregar_departamento(objeto_departamento3)
#asignar
objeto_edificio.asignar_administrador(objeto_administrador)
objeto_edificio.asociar_junta_propietarios(objeto_junta_propietarios)

#mostrar información 
objeto_edificio.obtener_info()
