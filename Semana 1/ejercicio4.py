salario = float(input('Ingrese el salario mensual: '))
personas_cargo = int(input('Ingrese número de personas a cargo:'))

tipo_linea = 'P'

if personas_cargo > 0:
  if personas_cargo == 1:
    if salario > 500:
      tipo_linea = 'O'
  elif personas_cargo < 5:
    if salario > 750:
      tipo_linea = 'O'
  else:
    if salario > 1000:
      tipo_linea = 'O'

  print('Tipo de línea al que puede acceder:',tipo_linea)

else:
  print('datos erróneos')
