def ingresa_fecha():
  fecha = ''
  while len(fecha) != 8 or fecha.isdigit() == False:
    fecha = input('Ingrese fecha: ')
  return fecha

def decomponer_fecha(fecha):
  anio = int(fecha[0:4])
  mes = int(fecha[4:6])
  dia = int(fecha[6:8])
  return anio,mes,dia


def validar_rangos(anio,mes,dia):
  if anio>= 1932 and anio<=2024:
    if mes>=1 and mes <=12:
      if dia>=1 and dia<=31:
        return True
  return False


def primer_filtro():
  while True:
    fecha = ingresa_fecha()
    anio,mes,dia = decomponer_fecha(fecha)
    if validar_rangos(anio,mes,dia):
      break
    else:
      print(f'La fecha {anio}/{mes}/{dia} es incorrecta”')
  return anio,mes,dia

def encontrar_maximo_dia(mes,anio):
  if mes == 2:
    if anio in bisiestos:
      return diccionario[mes][1]
    else:
      return diccionario[mes][0]
  else:
    return diccionario[mes]

def segundo_filtro():
  anio,mes,dia = primer_filtro()
  if dia <= encontrar_maximo_dia(mes,anio):
    print(f'La fecha {anio}/{mes}/{dia} es correcta')
  else:
    print(f'“El día {dia} es mayor que el máximo día del mes {mes}”')


diccionario = {1:31,2:(28,29),3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
bisiestos = []
for i in range(1932,2025,4):
  bisiestos.append(i)

segundo_filtro()
