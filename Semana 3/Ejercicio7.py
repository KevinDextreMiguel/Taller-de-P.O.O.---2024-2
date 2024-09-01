def ingresar():
  precion_segundo = float(input("Ingrese el precio por segundo: "))
  numero_llamadas = int(input('Ingrese el número de llamadas: '))
  return precion_segundo, numero_llamadas


def registrar_llamadas(numero_llamadas,precion_segundo):
  total = 0
  for i in range(numero_llamadas):
    hora = int(input("hora: "))
    minuto = int(input('minuto: '))
    segundo = int(input('segundo: '))
    total += hora *3600+ minuto *60 + segundo
  total *= precion_segundo
  print(f'total: {total}')


precion_segundo, numero_llamadas = ingresar()
registrar_llamadas(numero_llamadas,precion_segundo)
