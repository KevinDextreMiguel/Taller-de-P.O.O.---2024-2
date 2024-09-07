def ingresa_fecha():
  fecha = ''
  while fecha.isdigit() == False or len(fecha) != 8:
    fecha = input('Ingresa la fecha: ')
  return fecha

def decomponer_fecha():
  fecha = ingresa_fecha()
  AAAA = int(fecha[:4])
  MM = int(fecha[4:6])
  DD = int(fecha[6:8])
  return AAAA,MM,DD


def validar_fecha(AAAA,MM,DD):
  if AAAA >= 1932 and AAAA<2025:
    if MM >= 1 and MM <= 12:
      if DD >= 1 and DD:
        return True
  return False

def verifica_fecha():
  while True:
    AAAA,MM,DD = decomponer_fecha()
    if validar_fecha(AAAA,MM,DD):
      break
    else:
      print(f'La fecha {AAAA}/{MM}/{DD} es incorrecta')
  return AAAA,MM,DD


def retorna_dia_mayor(AAAA,MM):
  if MM == 2:
    if AAAA in bisiesto:
      return diccionario[MM][1]
    else:
      return diccionario[MM][0]
  return diccionario[MM]


def filtro_final():
  AAAA,MM,DD = verifica_fecha()
  dia_mayor = retorna_dia_mayor(AAAA,MM)
  if DD <= dia_mayor:
    print(f'La fecha {AAAA}/{MM}/{DD} es correcta')
  else:
    print(f'“El día {DD} es mayor que el máximo día del mes {MM}”')



diccionario = { 1:31,2:(28,29), 3:31,4:30,5:31,6:30,
               7:31,8:31,9:30,10:31,11:30,12:31}
bisiesto = []
for i in range(1932,2025,4):
  bisiesto.append(i)

filtro_final()
