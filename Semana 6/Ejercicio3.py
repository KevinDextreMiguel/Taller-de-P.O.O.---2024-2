from datetime import *

def ingresar_fecha():
  fecha = input('Ingrese fecha: ')
  formato = '%Y/%m/%d'
  fecha = datetime.strptime(fecha,formato)
  return fecha


def proximas_citas(fecha):
  dia = fecha.day
  mes = fecha.month
  anio = fecha.year
  calendario = list()

  if dia > 20:
    mes = mes + 1

  for i in range(8):
    if mes > 12:
      mes = 1
      anio += 1

    if fecha.weekday() == 6:
      dia = 21
    else:
      dia = 20
    
    fecha = datetime(anio,mes,dia)
    calendario.append(fecha)
    mes += 1

  return calendario

def mostrar_calendario(calendario):
  for fecha in calendario:
    print(fecha.strftime("%Y/%m/%d"))

#main
fecha = ingresar_fecha()
calendario = proximas_citas(fecha)
mostrar_calendario(calendario)
