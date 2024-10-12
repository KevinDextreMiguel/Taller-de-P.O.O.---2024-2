class Encomienda:
  __diccionario = {}
  def __init__(self, codigo, remitente,destinatario,direccionEntrega,pesoKg,volumenm3,costokg,costom3):
    self.__codigo = codigo
    self.__remitente = remitente
    self.__destinatario = destinatario
    self.__direccionEntrega = direccionEntrega
    self.__pesoKg = pesoKg
    self.__volumenm3 = volumenm3
    self.__costokg = costokg
    self.__costom3 = costom3

    #get
  def getCodigo(self):
    return self.__codigo
  def getRemitente(self):
    return self.__remitente
  def getDestinatario(self):
    return self.__destinatario
  def getDireccionEntrega(self):
    return self.__direccionEntrega
  def getPesoKg(self):
    return self.__pesoKg
  def getVolumenm3(self):
    return self.__volumenm3
  def getCostokg(self):
    return self.__costokg
  def getCostom3(self):
      return self.__costom3
    #set
  def setCodigo(self,codigo):
    self.__codigo = codigo
  def setRemitente(self,remitente):
    self.__remitente = remitente
  def setDestinatario(self,destinatario):
    self.__destinatario = destinatario
  def setDireccionEntrega(self,direccionEntrega):
    self.__direccionEntrega = direccionEntrega
  def setPesoKg(self,pesoKg):
    self.__pesoKg = pesoKg
  def setVolumenm3(self,volumenm3):
    self.__volumenm3 = volumenm3
  def setCostokg(self,costokg):
    self.__costokg = costokg
  def setCostom3(self,costom3):
      self.__costom3 = costom3
    
  def costo_por_peso(self):
    return self.__pesoKg * self.__costokg
  def costo_por_volumen(self):
    return self.__volumenm3 * self.__costom3
  def valor_envio(self):
    return self.costo_por_peso() + self.costo_por_volumen()
  def agregar(self):
    self.__diccionario[self.__codigo] = self.__remitente,self.__destinatario,self.__direccionEntrega,self.__pesoKg,self.__volumenm3,self.valor_envio()
  def listar(self):
    for clave,valor in self.__diccionario.items():
      print(f'{clave}: {valor}')

    


def opcion():
  print('1. Agregar encomienda')
  print('2. Listar encomiendas')
  print('3. Salir')
  opcion = -1
  while opcion<1 or opcion>3:
    try:
      opcion = int(input('Ingrese una opcion: '))
    except:
      print('Opcion invalida')
  return opcion
              
def menu():
  while True:
    opc = opcion()
    if opc == 1:
      codigo = input('Código: ')
      remitente = input('Remitente: ')
      destinatario = input('Destinatario: ')
      direccionEntrega = input('Dirección de Entrega: ')
      pesoKg = float(input('Peso en Kg: '))
      volumenm3 = float(input('Volumen en m3: '))
      costokg = float(input('Costo por Kg: '))
      costom3 = float(input('Costo por m3: '))
      obj = Encomienda(codigo, remitente,destinatario,direccionEntrega,pesoKg,volumenm3,costokg,costom3)
      obj.agregar()
    elif opc == 2:
      obj1.listar()
    elif opc == 3:
      break
                           
#main
obj1 = Encomienda(1,2,3,4,5,6,7,8)
obj1.agregar()
menu()
