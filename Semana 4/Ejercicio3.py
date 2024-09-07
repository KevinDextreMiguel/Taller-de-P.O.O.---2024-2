def menu():
  opcion = -1
  print('(1) Añadir cliente')
  print('(2) Eliminar cliente')
  print('(3) Listar todos los clientes')
  print('(4) Terminar. ')
  while opcion<1 or opcion>4:
    try:
      opcion = int(input('Ingresa la opcion: '))
    except ValueError:
      print('Error')
  return opcion

def registra():
  dni = input('Ingresa el DNI del cliente: ')
  nombre = input('Ingresa el nombre del cliente: ')
  direccion = input('Ingresa la direccion del cliente: ')
  telefono = input('Ingresa el telefono del cliente: ')
  email = input('Ingresa el email del cliente: ')
  preferente = bool(input('Ingresa preferente Sì(1) No(0): '))
  diccionario[dni] = {'nombre':nombre,'direccion':direccion,'telefono':telefono,
                      'email':email,'preferente':preferente}


def eliminar():
  dni = input('Ingresa el DNI del cliente: ')
  if dni in diccionario.keys():
    diccionario.pop(dni)
  else:
    print('DNI no encontrado')


def listar():
  print('DNI Nombre Dirección Teléfono Email Preferente')
  for clave,valor in diccionario.items():
    print(f'{clave} {valor["nombre"]} {valor["direccion"]} {valor["telefono"]} {valor["email"]} {valor["preferente"]}')


def main():
  while True:
    opcion = menu()
    if opcion == 1:
      registra()
    elif opcion == 2:
      eliminar()
    elif opcion == 3:
      listar()
    else:
      break


diccionario = dict()
main()
