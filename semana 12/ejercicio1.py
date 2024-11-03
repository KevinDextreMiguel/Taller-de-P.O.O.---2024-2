import pandas as pd

def leer():
  titanic = pd.read_csv('titanic.csv',sep=';',decimal=',',index_col=0)
  return titanic


df = leer()
df = pd.DataFrame(df)

print('Dimensión ',df.shape)
print('Nùmero de elementos ',df.size)
print('nombre de columnas: ',df.columns)
print('Tipos de datos: ',df.dtypes)
print('10 primeras filas',df.head(10))
print('10 ultimas filas',df.tail(10))
print('============================')
id = 148
print('id 148: ',df.loc[id])
print('============================')
print('Mostrar las filas pares del DataFrame')
print(df.iloc[range(1,df.shape[0],2)])
print('============================')
#Mostrar los nombres de las personas que iban en primera clase ordenadas 
#alfabéticamente.
print('Mostrar Nombres')
print(df[df['Pclass']==1]['Name'].sort_values())
print('============================')
#Mostrar por pantalla el porcentaje de personas que sobrevivieron y murieron.
print('============================')
print('Mostrar el porcentaje de personas que sobrevivieron y murieron. ')
porcentaje = df['Survived'].value_counts(normalize=True)*100
print(porcentaje)
print('============================')
print('Eliminar del DataFrame los pasajeros con edad desconocida')
df.dropna(subset=['Age'])
print(df)
