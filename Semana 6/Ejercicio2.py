from datetime import datetime

def convertir_fecha(fecha):
  fecha = datetime.strptime(fecha, "%Y/%m/%d")
  return fecha

def ingresa_fecha():
  fecha_desembolso = input("Ingrese la fecha de desembolso YYYY/MM/DD: ")
  fecha_pago = input("Ingrese la fecha de pago YYYY/MM/DD: ")
  fecha_desembolso = convertir_fecha(fecha_desembolso)
  fecha_pago = convertir_fecha(fecha_pago)
  return fecha_desembolso, fecha_pago

def calcular_dias_transcurridos(fecha_desembolso, fecha_pago):
  dias_transcurridos = (fecha_pago - fecha_desembolso).days
  return dias_transcurridos

def ingresa_monto_interes():
  capital = float(input("Ingrese el capital: "))
  interes = float(input("Ingrese el interés: "))
  return capital,interes


def calcular(capital,interes,dias):
  factor = (1+interes)**(dias/360) - 1
  interes_total = capital * factor
  total = capital + interes_total
  print(f'Interes: {interes_total:.2f}')
  print(f'Total a pagar: {total:.2f}')


fecha_desembolso, fecha_pago = ingresa_fecha()
capital,interes = ingresa_monto_interes()
dias = calcular_dias_transcurridos(fecha_desembolso, fecha_pago)
calcular(capital,interes,dias)
