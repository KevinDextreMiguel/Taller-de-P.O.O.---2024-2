from datetime import datetime

def ingresa_fecha():
  fecha = input("Ingrese una fecha en formato YYYY/MM/DD: ")
  fecha = datetime.strptime(fecha, "%Y/%m/%d")
  return fecha

def dias_trancurridos(fecha_nacimiento,fecha_actual):
  dias = (fecha_actual - fecha_nacimiento).days
  print(f'Cantidad de dìas que pasaron desde tu nacimeinto {dias}')

def determina_dia_semana(fecha_nacimiento):
  dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
  dia_semana = dias_semana[fecha_nacimiento.weekday()]
  print(f'El dìa fue: {dia_semana}')

def obtner_dias_siguiente_cumpleanios(fecha_nacimiento,fecha_actual):
  proximo_cumpleanios = datetime(fecha_actual.year,fecha_nacimiento.month,fecha_nacimiento.day)
  if proximo_cumpleanios < fecha_actual:
    proximo_cumpleanios = datetime(fecha_actual.year+1,fecha_nacimiento.month,fecha_nacimiento.day)
  dias = (proximo_cumpleanios - fecha_actual).days
  print(f'Cantidad de dìas que faltan para tu cumpleaños {dias}')

                                   

fecha_actual = datetime.now()

fecha_nacimiento = ingresa_fecha()
dias_trancurridos(fecha_nacimiento,fecha_actual)
determina_dia_semana(fecha_nacimiento)
obtner_dias_siguiente_cumpleanios(fecha_nacimiento,fecha_actual)
