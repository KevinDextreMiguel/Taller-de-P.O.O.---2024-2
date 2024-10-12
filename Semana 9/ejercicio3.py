class Pasajero:
  def __init__(self, numero_pasaporte,nombre,edad,tipo_asiento):
    self.__numero_pasaporte = numero_pasaporte
    self.__nombre = nombre
    self.__edad = edad
    self.__tipo_asiento = tipo_asiento
  
  #set
  def setNumero_pasaporte(self,numero_pasaporte):
    self.__numero_pasaporte = numero
  def setNombre(self,nombre):
    self.__nombre = nombre
  def setEdad(self,edad):
    self.__edad = edad
  def setTipo_asiento(self,tipo_asiento):
    self.__tipo_asiento = tipo_asiento
  #get
  def getNumero_pasaporte(self):
    return self.__numero
  def getNombre(self):
    return self.__nombre
  def getEdad(self):
    return self.__edad
  def getTipo_asiento(self):
    return self.__tipo_asiento
  
  def __str__(self):
    return f'{self.__numero_pasaporte} {self.__nombre} {self.__edad} {self.__tipo_asiento}'



class Vuelo:
  def __init__(self, numero_vuelo,ciudad_partida,ciudad_llegada,hora_salida,hora_llegada):
    self.__numero_vuelo = numero_vuelo
    self.__ciudad_partida = ciudad_partida
    self.__ciudad_llegada = ciudad_llegada
    self.__hora_salida = hora_salida
    self.__hora_llegada = hora_llegada
    self.__pasajeros = []
  #get
  def getNumero_vuelo(self):
    return self.__numero_v
  def getCiudad_partida(self):
    return self.__ciudad_partida
  def getCiudad_llegada(self):
    return self.__ciudad_llegada
  def getHora_salida(self):
    return self.__hora_salida
  def getHora_llegada(self):
    return self.__hora_llegada
  def getPasajeros(self):
    return self.__pasajeros
  #set
  def setNumero_vuelo(self,numero_vuelo):
    self.__numero_vuelo = numero_vuelo
  def setCiudad_partida(self,ciudad_partida):
    self.__ciudad_partida = ciudad_partida
  def setCiudad_llegada(self,ciudad_llegada):
    self.__ciudad_llegada = ciudad
  def setHora_salida(self,hora_salida):
    self.__hora_salida = hora_salida
  def setHora_llegada(self,hora_llegada):
    self.__hora_llegada = hora_llegada
  
  def agregar_pasajero(self,obj_pasajero):
    self.__pasajeros.append(obj_pasajero)
  def listar_pasajeros(self):
    print(f'Vuelo: {self.__numero_vuelo}, Ciudad Origen: {self.__ciudad_partida}')
    for pasajero in self.__pasajeros:
      print(pasajero)



obj_pasajero1 = Pasajero('12344','kevin',23,'tipoA')
obj_pasajero2 = Pasajero('3456','Cosner',24,'tipoA')
obj_vuelo = Vuelo('125','Lima,','Bogotá','12:300','14:30')
obj_vuelo.agregar_pasajero(obj_pasajero1)
obj_vuelo.agregar_pasajero(obj_pasajero2)
obj_vuelo.listar_pasajeros()
