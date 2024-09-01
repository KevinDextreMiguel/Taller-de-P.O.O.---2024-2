def imprimir(lista):
  print('============')
  for i in lista:
    print(i)

def existe_codigo(lista,codigo):
  for i in lista:
    if codigo == i[0]:
      return True
  return False

def ordenar_codigo():
  longitud = len(lista)
  for i in range(longitud):
    for j in range(longitud):
      if lista[i][0] < lista[j][0]:
        aux = lista[i]
        lista[i] = lista[j]
        lista[j] = aux
  return lista

def registrar():
  salir = 's'
  while salir == 's' or salir == 'S':
    while True:
      codigo = input('Ingrese código: ')
      if existe_codigo(lista,codigo):
        print('El código ya existe')
      else:
        break
    apellido = input('Ingrese apellido: ')
    nombre = input('Ingrese nombre: ')
    aux = [codigo,apellido,nombre]
    lista.append(aux)

    salir = input('¿Desea continuar? (S/N): ')


lista=[]
registrar()
imprimir(lista)
lista = ordenar_codigo()
imprimir(lista)
ordenar_apellido = sorted(lista, key=lambda x: x[1])
imprimir(ordenar_apellido)
