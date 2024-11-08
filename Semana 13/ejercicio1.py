import pandas as pd
import numpy as np

class Calificacion:
  def __init__(self, codigo,nombre,modalidad,pc1,pc2):
    self.__codigo = codigo
    self.__nombre = nombre
    self.__modalidad = modalidad
    self.__pc1 = pc1
    self.__pc2 = pc2
    self.__nota_final = 0
  #get
  @property
  def codigo(self):
    return self.__codigo
  @property
  def nombre(self):
    return self.__nombre
  @property
  def modalidad(self):
    return self.__modalidad
  @property
  def pc1(self):
    return self.__pc1
  @property
  def pc2(self):
    return self.__pc2
  @property
  def nota_final(self):
    return self.__nota_final
  #set
  @codigo.setter
  def codigo(self, codigo):
    self.__codigo = codigo
  @nombre.setter
  def nombre(self, nombre):
    self.__nombre = nombre
  @modalidad.setter
  def modalidad(self, modalidad):
    self.__modalidad = modalidad
  @pc1.setter
  def pc1(self, pc1):
    self.__pc1 = pc1
  @pc2.setter
  def pc2(self, pc2):
    self.__pc2 = pc2
  @nota_final.setter
  def nota_final(self, nota_final):
    self.__nota_final = nota_final
  
  def __str__(self):
    return f'Còdigo:{self.__codigo}\nNombres:{self.__nombre}\nModalidad{self.__modalidad}\nNota Final:{    self.__nota_final}'


class CalificacionEPE(Calificacion):
  def __init__(self, codigo,nombre,modalidad,pc1,pc2,tp,tf):
    super().__init__(codigo,nombre,modalidad,pc1,pc2)
    self.__trabajo_parcial = tp
    self.__trabajo_final = tf
  
  def calcular_nota_final(self):
    self.nota_final = self.pc1*0.2 + self.pc2*0.2 + self.__trabajo_parcial*0.3 + self.__trabajo_final*0.3

class CalificacionPG(Calificacion):
  def __init__(self, codigo,nombre,modalidad,pc1,pc2,pf,eb):
    super().__init__(codigo,nombre,modalidad,pc1,pc2)
    self.__proyecto_final = pf
    self.__examen_final = eb
  
  def calcular_nota_final(self):
    self.nota_final = self.pc1*0.15 + self.pc2*0.15 + self.__proyecto_final*0.4 + self.__examen_final*0.3


class Manejadora:
  def __init__(self):
    self.__calificaciones = []
  def agregar_calificacion(self, objeto):
    objeto.calcular_nota_final()
    self.__calificaciones.append(objeto)
  def mostrar_calificaciones(self):
    for objeto in self.__calificaciones:
      print('===============================')
      print(objeto)
  def existe_calificacion(self,codigo):
    for objeto in self.__calificaciones:
      if objeto.codigo == codigo:
        return True
    return False
  def estadistica(self):
    notas_finales = []
    for objeto in self.__calificaciones:
      notas_finales.append(objeto.nota_final)
    mayor = np.max(notas_finales)
    menor = np.min(notas_finales)
    media = np.mean(notas_finales)
    mediana = np.median(notas_finales)
    print(f'Mayor:{mayor}\nMenor:{menor}\nMedia:{media}\nMediana:{mediana}')
    return notas_finales
  def guardar_excel(self):
    codigos = []
    nombres = []
    modalidades = []
    notas_finales = self.estadistica()
    for objeto in self.__calificaciones:
      codigos.append(objeto.codigo)
      nombres.append(objeto.nombre)
      modalidades.append(objeto.modalidad)
    datos = {'Codigo':codigos,'Nombre':nombres,
             'Modalidad':modalidades,'Nota Final':notas_finales}
    df = pd.DataFrame(datos)
    df.to_excel('calificaciones.xlsx',index=False)
    print('Archivo guardado')


def opciones():
  opcion = -1
  print('1. Agregar calificacion EPE')
  print('2. Agregar calificacion PG')
  print('3. Mostrar calificaciones')
  print('4. Estadistica')
  print('5. Guardar Excel')
  print('6. Salir')
  while opcion < 1 or opcion > 6:
    try:
      opcion = int(input('Ingrese una opcion: '))
    except:
      print('Ingrese una opcion valida')
  return opcion

def validar_nota(mensaje):
  nota = -1
  while nota < 0 or nota > 20:
    nota = float(input(mensaje))
  return nota

def ingresar_datos():
  while True:
    codigo = input('Ingrese el codigo: ')
    if manejedora.existe_calificacion(codigo):
      print('Ya existe con ese código')
    else:
      break
  nombre = input('Ingrese el nombre: ')
  modalidad = input('Ingrese la modalidad: ')
  pc1 = validar_nota('Ingrese la nota de PC1: ')
  pc2 = validar_nota('Ingrese la nota de PC2: ')
  return codigo,nombre,modalidad,pc1,pc2

def menu():
  while True:
    opcion = opciones()
    if opcion == 1:
      codigo,nombre,modalidad,pc1,pc2 = ingresar_datos()
      tp = validar_nota('Ingrese la nota del trabajo parcial: ')
      tf = validar_nota('Ingrese la nota del trabajo final: ')
      objeto = CalificacionEPE(codigo,nombre,modalidad,pc1,pc2,tp,tf)
      manejedora.agregar_calificacion(objeto)
    elif opcion == 2:
      codigo,nombre,modalidad,pc1,pc2 = ingresar_datos()
      pf = validar_nota('Ingrese la nota del proyecto final: ')
      eb = validar_nota('Ingrese la nota del examen final: ')
      objeto = CalificacionPG(codigo,nombre,modalidad,pc1,pc2,pf,eb)
      manejedora.agregar_calificacion(objeto)
    elif opcion == 3:
      manejedora.mostrar_calificaciones()
    elif opcion == 4:
      manejedora.estadistica()
    elif opcion == 5:
      manejedora.guardar_excel()
    else:
      break


manejedora = Manejadora()
menu()
