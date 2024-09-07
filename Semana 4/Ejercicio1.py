def ingresa_transporte():
  transporte = ''
  while transporte != 'A' and transporte != 'T' and transporte != 'P' and transporte != 'X':
    transporte = input('Ingresa el tipo de transporte: ')
  return transporte 

def ingresa_duracion():
  tiempo = -1
  while tiempo<1:
    try:
      tiempo = int(input('Ingresa la duracion del viaje: '))
    except ValueError:
      print('Error')
  return tiempo

def ingresa_momento_dia():
  momento = -1
  while momento<1 or momento>4:
    try:
      momento = int(input('Ingresa el momento: '))
    except ValueError:
      print('Error')
  return momento

def ingresa_ruta():
  ruta = ''
  while ruta != 'A' and ruta != 'B'  and ruta != 'C' and ruta != 'O':
    ruta = input('Ingresa la ruta: ')
  return ruta 

def guardar_datos():
  cont = 1
  while True:
    transporte = ingresa_transporte()
    if transporte == 'X':
      break
    duracion = ingresa_duracion()
    momento = ingresa_momento_dia()
    ruta = ingresa_ruta()
    diccionario[cont] = transporte,duracion,momento,ruta
    cont+=1


def cantidad_medio_transporte():
  lista_transporte = []
  for valor in diccionario.values():
    lista_transporte.append(valor[0])
  print('Reporte')
  print('Cantidad de usuarios por medio de transporte')
  print('Auto propio: ',lista_transporte.count('A'))
  print('Privado: ',lista_transporte.count('T'))
  print('Transporte público: ',lista_transporte.count('P'))


def momento_dia_mas_viajado():
  lista_momento = []
  lista_contadores = []
  for valor in diccionario.values():
    lista_momento.append(valor[2])
  
  for i in range(4):
    lista_contadores.append(lista_momento.count(i+1))
  mayor = max(lista_contadores)
  print('Momentos con mayor cantidad de viajes son:')
  for i in range(len(lista_contadores)):
    if  lista_contadores[i] == mayor:
      print(i+1,end=', ')
  print()
  
def tiempo_promedio_ruta():
  contA = contB = contC = contO = 0
  sumaA = sumaB = sumaC = sumaO = 0
  for valor in diccionario.values():
    if valor[3] == 'A':
      contA+=1
      sumaA+=valor[1]
    elif valor[3] == 'B':
      contB+=1
      sumaB+=valor[1]
    elif valor[3] == 'C':
      contC+=1
      sumaC+=valor[1]
    else:
      contO+=1
      sumaO+=valor[1]

  if contA != 0:
    sumaA = sumaA/contA
  if contB != 0:
    sumaB = sumaB/contB
  if contC != 0:
    sumaC = sumaC/contC
  if contO != 0:
    sumaO = sumaO/contO

  print('Tiempo promedio de viaje por ruta son:')
  print(f'Av. Arequipa: {sumaA}')
  print(f'Av. Brasil: {sumaB}')
  print(f'Paseo de la República: {sumaC}')
  print(f'Otra ruta: {sumaO}')


diccionario = dict()
guardar_datos()
cantidad_medio_transporte()
momento_dia_mas_viajado()
tiempo_promedio_ruta()
