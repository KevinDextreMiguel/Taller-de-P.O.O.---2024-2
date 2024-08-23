def ingresa_tamanio():
  tamanio = ''
  while tamanio != 'pequeño' and tamanio != 'normal' and tamanio != 'gigante':
    try:
      tamanio = input("Ingrese el tamaño (pequeño, normal y el gigante): ")
    except ValueError:
      print('error')
    
  return tamanio


def ingresar_cantidad():
  n=-1
  while n<0:
    try:
      n = int(input("Ingrese cantidad: "))
    except ValueError:
      print('error')
    
  return n

def metodo_pago():
  metodo = ''
  while metodo != 'Débito' and metodo != 'Crédito' and metodo != 'Efectivo':
    try:
      metodo =input("Ingrese tipo de pago (D=Débito, C=Crédito, E=Efectivo): ")
    except ValueError:
      print('error')
    
  return metodo


def calcula():
  tamanio = ingresa_tamanio()
  precio = cargo = descuento = 0
  if tamanio == 'pequeño':
    precio = 15
  elif tamanio == 'normal':
    precio = 25
  else:
    precio = 30

  cantidad = ingresar_cantidad()
  total = precio * cantidad
  metodo = metodo_pago()

  if metodo == 'Débito':
    cargo = 0.03
  elif metodo == 'Crédito':
    cargo = 0.05
  else:
    descuento = 0.02
  
  monto_final = total + total * cargo - total * descuento
  
  print('=============================')
  print('Número de panes con chicharrón comprados: ',cantidad)
  print('El tamaño comprado: ',tamanio)
  print('El precio del pan con chicharrón comprado: ',precio)
  print('Tipo de pago (D=Débito, C=Crédito, E=Efectivo): ',metodo)
  print('Total sin cargo o descuento: ',total)
  print('Valor del cargo: ',cargo*total)
  print('Valor del descuento: ',descuento*total)
  print('Total a pagar: ',monto_final)


def main():
  n = 1
  while n==1:
    calcula()
    try:
      n = int(input("1 para continuar: "))
    except ValueError:
      print('error')


#main
main()
