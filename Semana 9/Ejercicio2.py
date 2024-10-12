class Terreno:
  __diccionario = {}
  def __init__(self,codigo,ubicacion,area,valor_m2_comercial,valorm2predial):
    self.__codigo = codigo
    self.__ubicacion = ubicacion
    self.__area = area
    self.__valor_m2_comercial = valor_m2_comercial
    self.__valorm2predial = valorm2predial
  #get
  def getCodigo(self):
    return self.__codigo
  def getUvbacion(self):
    return self.__ubicacion
  def getArea(self):
    return self.__area
  def valor_m2_comercial(self):
    return self.__valor_m2_comercial
  def valor_m2_predial(self):
    return self.__valorm2predial
  #set
  def setCodigo(self,codigo):
    self.__codigo = codigo
  def setUbicacion(self,ubicacion):
    self.__ubicacion = ubicacion
  def setArea(self,area):
    self.__area = area
  def setValor_m2_comercial(self,valor_m2_comercial):
    self.__valor_m2_comercial = valor_m2_comercial
  def setValor_m2_predial(self,valorm2predial):
    self.__valorm2predial = valorm2predial

  def valor_predial_terreno(self):
    return self.__area * self.__valorm2predial
  def valor_comercial_terreno(self):
    return self.__area * self.__valor_m2_comercial
  def margen_ganancia(self):
    return self.valor_comercial_terreno() - self.valor_predial_terreno()

  def agregar(self):
    self.__diccionario[self.__codigo] = self.__ubicacion,self.__area,self.valor_comercial_terreno(),self.valor_predial_terreno(),self.margen_ganancia()
  def listar(self):
    for clave,valor in self.__diccionario.items():
      print(f'{clave}: {valor}')


obj_terreno = Terreno("asdf","28 de Julio",1000,50000,1000)
obj_terreno.agregar()
obj_terreno.listar()
obj_terreno = Terreno("werr","3 de mayo",2000,70000,4000)
obj_terreno.agregar()
obj_terreno.listar()
