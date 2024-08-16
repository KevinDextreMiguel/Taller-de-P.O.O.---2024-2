cantidad = int(input('Ingrese la cantidad de alambre requerido: '))

cantidad500 = cantidad // 500
residuo500 = cantidad % 500

cantidad300 = residuo500 // 300
residuo300 = residuo500 % 300

cantidad75 = residuo300 // 75
residuo75 = residuo300 % 75

print('Se requiere:')
print(cantidad500, 'rollo de 500 metros')
print(cantidad300, 'rollo de 300 metros')
print(cantidad75, 'rollo de 75 metros')
print('El último rollo tendrá',residuo75, 'metros')
