from datetime import datetime

def ingresar_fecha():
  fecha = input("Ingrese la fecha de la primera cita YYYY/MM/DD: ")
  fecha = datetime.strptime(fecha, "%Y/%m/%d")
  return fecha

def fechas_proxima_cita(fecha):
  dia = fecha.day
  mes = fecha.month
  anio = fecha.year
  calendario = []

  if dia < 20:
    mes = mes
  else:
    mes = mes + 1

  for i in range(8):
    if mes > 12:
      mes = 1
      anio = anio + 1

    if fecha.weekday() == 6:
      dia = 21
    else:
      dia = 20

    fecha = datetime(anio, mes, dia)
    calendario.append(fecha)

    mes += 1

  return calendario

def mostrar_calendario(calendario):
  for fecha in calendario:
    print(fecha.strftime("%Y/%m/%d"))

fecha = ingresar_fecha()
calendario = fechas_proxima_cita(fecha)
mostrar_calendario(calendario)
