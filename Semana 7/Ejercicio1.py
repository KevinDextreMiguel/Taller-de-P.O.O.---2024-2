class Cliente:
  def __init__(self, nombre, dni, direccion,telefono,correo,preferente):
    self.__nombre = nombre
    self.__dni = dni
    self.__direccion = direccion
    self.__telefono = telefono
    self.__correo = correo
    self.__preferente = preferente

  #get
  def get_nombre(self):
    return self.__nombre
  def get_dni(self):
    return self.__dni
  def get_direccion(self):
    return self.__direccion
  def get_telefono(self):
    return self.__telefono
  def get_correo(self):#edad = 16 --> mayor = False
    return self.__correo

  #set
  def set_nombre(self,nombre):
    self.__nombre = nombre
  def set_direccion(self,direccion):
    self.__direccion = direccion
  def set_telefono(self,telefono):
    self.__telefono = telefono

  def __str__(self):
    return f"Nombre: {self.__nombre}\nDNI: {self.__dni}\nDirección: {self.__direccion}\nTeléfono: {self.__telefono}\nCorreo: {self.__correo}"


#creamos una clase donde se manejarán
#los datos de los clientes
class ListaCliente:
  def __init__(self):
    self.__lista = []
  def agregar_cliente(self,cliente):
    self.__lista.append(cliente)
  def existe_cliente(self,dni):
    for cliente in self.__lista:
      if cliente.get_dni() == dni:
        return True
    return False
  def eliminar_cliente(self,dni):#(indice)
    for i in range(len(self.__lista)):
      if self.__lista[i].get_dni() == dni:
        self.__lista.pop(i) #self.__lista.remove(cliente)
        break
  def mostrar_clientes(self):
    for cliente in self.__lista:
      print(cliente)
  def mostrar_nombre(self,nombre):
    for cliente in self.__lista:
      if cliente.get_nombre() == nombre:
        print(cliente)
  def actualizar(self,indice,direccion):
    self.__lista[indice].set_direccion(direccion)


#se crea las opciones de donde se va
# realizar el proceso CRUD
def ingresa_opcion():
  opcion = -1
  print('(1) Añadir cliente')
  print('(2) Buscar cliente')
  print('(3) Actualizar cliente')
  print('(4) Eliminar cliente')
  print('(5) Listar todos los clientes')
  print('(6) Terminar')
  while opcion < 1 or opcion > 6:
    opcion = int(input('Ingrese una opción: '))
  return opcion

def ingresar_datos():
  telefono = ''
  while True:
    dni = input('Ingrese el DNI: ')
    if obj_lista_cliente.existe_cliente(dni):
      print('El cliente ya existe')
    else:
      break
  nombre = input('Ingrese el nombre: ')
  direccion = input('Ingrese la dirección: ')
  while len(telefono) != 9:
    telefono = input('Ingrese el teléfono: ')
  correo = input('Ingrese el correo: ')
  preferente = bool(input('¿Es preferente? (1/0): '))
  objeto_cliente = Cliente(nombre,dni,direccion,telefono,correo,preferente)
  return objeto_cliente

def menu():
  while True:
    opcion = ingresa_opcion()
    if opcion == 1:
      objeto_cliente = ingresar_datos()
      obj_lista_cliente.agregar_cliente(objeto_cliente)
      print('Exitoso')
    elif opcion == 2:
      nombre = input('Ingrese el nombre: ')
      obj_lista_cliente.mostrar_nombre(nombre)
    elif opcion == 3:
      direccion = input('Ingrese la dirección: ')
      indice = int(input('Ingrese el índice: '))
      obj_lista_cliente.actualizar(indice,direccion)
      print('Exitoso')
    elif opcion == 4:
      dni = input('Ingrese el DNI: ')
      obj_lista_cliente.eliminar_cliente(dni)
      print('Eliminado')
    elif opcion == 5:
      obj_lista_cliente.mostrar_clientes()
    else:
      break

#main
obj_lista_cliente = ListaCliente()
menu()
