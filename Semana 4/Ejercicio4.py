import re
def imprimir(texto):
  print('============================')
  print(texto)

def convertir(texto):
  diccionario = dict()
  imprimir(texto)
  texto = re.sub(r'[^\w\s]', '', texto)
  imprimir(texto)
  texto = texto.lower()
  imprimir(texto)
  lista = texto.split()
  for palabra in lista:
    diccionario[palabra] = diccionario.get(palabra,0)+1
  print(f'Cantidad por palabra: {diccionario}')

  return diccionario
  
def ordenar_diccionario(diccionario):
  lista = list()
  for clave,valor in diccionario.items():
    lista.append((valor,clave))

  lista.sort(reverse=True)
  for valor,clave in lista:
    print(clave,valor)


texto = """
¡Oh! Que madre tan bella. ¿Será que La madre de Juan es hermana de Pedro?
Juan va con ella a todos lados; es decir no la deja sola ni para ir al mercado.
Juan le dice a su madre que compre piña, mango, melón, patilla porque son 
nutritivos.
La madre de Juan le enseña las vocales: a, e, i, o, u.
En la casa de Juan hay muchos colores: azul, amarillo, rojo, verde…
La madre de Juan le enseña que Simón Bolívar dijo:
"Un ser sin estudio es un ser incompleto".
"""

diccionario = convertir(texto)
ordenar_diccionario(diccionario)
