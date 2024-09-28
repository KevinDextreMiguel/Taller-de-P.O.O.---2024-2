def ingresa_opcion():
  opcion = -1
  print('[1] Registra calificaciones')
  print('[2] Reporte de calificaciones')
  print('[3] Estadísticas de calificaciones')
  print('[4] Salir')
  while opcion < 1 or opcion > 4:
    try:
      opcion = int(input('Ingrese una opción: '))
    except ValueError:
      print('Debe ingresar un número')
  return opcion

def registrar():
  codigo = input('Ingrese el código: ')
  nombres = input('Ingrese el nombre: ')
  n1 = float(input('Ingrese la nota 1: '))
  n2 = float(input('Ingrese la nota 2: '))
  n3 = float(input('Ingrese la nota 3: '))
  n4 = float(input('Ingrese la nota 4: '))
  menor = min(n1,n2,n3,n4)
  promedio = (n1+n2+n3+n4-menor)/3
  promedio = round(promedio,2)
  aprobado = 'Aprobado'
  if promedio < 15:
    aprobado = 'Reprobado'
  alumnos['u202222'] = {'Nombre':nombres,'Promedio':promedio,'menor':menor,'Aprobado':aprobado}


def listar():
  for clave,valor in alumnos.items():
    print(clave,valor)

def estadisticas():
  aprobados = 0
  reprobados = 0
  lista = list()
  for clave,valor in alumnos.items():
    lista.append(valor['Promedio'])
    if valor['Aprobado'] == 'Aprobado':
      aprobados += 1
    else:
      reprobados += 1
  print(f'Aprobados: {aprobados}')
  print(f'Reprobados: {reprobados}')
  print(f'Promedio: {sum(lista)/len(lista)}')
  print(f'Mayor: {max(lista)}')
  print(f'Menor: {min(lista)}')


def menu():
  while True:
    opcion = ingresa_opcion()
    if opcion == 1:
      registrar()
    elif opcion == 2:
      listar()
    elif opcion == 3:
      estadisticas()
    else:
      break


alumnos = dict()
menu()
