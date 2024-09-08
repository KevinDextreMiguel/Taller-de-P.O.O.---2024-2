def pedir_medio_transporte():
  transporte = ''
  while transporte != 'A' and transporte != 'T' and transporte != 'P' and transporte != 'X':
    transporte = input("Medio de transporte: ")
  return transporte


def pedir_ruta():
  ruta = ''
  while ruta != 'A' and ruta != 'B' and ruta != 'C' and ruta != 'O':
    ruta = input("Ruta: ")
  return ruta

def pedir_tiempo():
  tiempo = -1
  while tiempo < 1:
    try:
      tiempo = int(input("Tiempo de viaje: "))
    except:
      print('error')
  return tiempo

def pedir_momento ():
  momento = -1
  while momento < 1 or momento > 4:
    try:
      momento = int(input("momento de viaje: "))
    except:
      print('error')
  return momento

def registrar_datos():
  cont = 1
  while True:
    medio_transporte = pedir_medio_transporte()
    if medio_transporte == 'X':
      break
    ruta = pedir_ruta()
    tiempo = pedir_tiempo()
    momento = pedir_momento()
    diccionario[cont] = medio_transporte, tiempo, momento,ruta
    cont += 1



def momentos_mayor_viaje():
  momentos = list()
  dict_contador = dict()
  for valor in diccionario.values():
      momentos.append(valor[2])
  
  for i in momentos:
      dict_contador[i]=dict_contador.get(i,0)+1
  mayor = max(dict_contador.values())
  print('Momentos con mayor cantidad de viajes son:')
  for clave,valor in dict_contador.items():
    if valor == mayor:
      print(clave,end=',')
  print()
      
def cantidad_medio_transporte():
  medios_transporte = []
  for valor in diccionario.values():
      medios_transporte.append(valor[0]) 
  print('Reporte')
  print('Cantidad de usuarios por medio de transporte')
  print('Auto propio: ',medios_transporte.count('A'))
  print('Privado: ',medios_transporte.count('T'))
  print('Transporte público: ',medios_transporte.count('P'))




def tiempo_promedio_ruta():
  contA = contB = contC = contO = 0
  sumaA = sumaB = sumaC = sumaO = 0
  for valor in diccionario.values():
    if valor[3] == 'A':
      sumaA += valor[1]
      contA += 1
    elif valor[3] == 'B':
      sumaB += valor[1]
      contB += 1
    elif valor[3] == 'C':
      sumaC += valor[1]
      contC += 1
    else:
      sumaO += valor[1]
      contO += 1

  if contA != 0:
    sumaA = sumaA/contA
  if contB != 0:
    sumaB = sumaB/contB
  if contC != 0:
    sumaC = sumaC/contC
  if contO != 0:
    sumaO = sumaO/contO

  print('Tiempo promedio por ruta')
  print('Ruta A: ',sumaA)
  print('Ruta B: ',sumaB)
  print('Ruta C: ',sumaC)
  print('Ruta O: ',sumaO)

diccionario = dict()
registrar_datos()
cantidad_medio_transporte()
momentos_mayor_viaje()
tiempo_promedio_ruta()
