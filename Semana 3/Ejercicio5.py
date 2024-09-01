def determinar_letra():
  letra = input('Ingrese una letra: ')
  if letra.isupper():
    print('Es mayúscula')
  elif letra.islower():
    print('Es minúscula')
  else:
    print('No es una letra')
  

determinar_letra()
