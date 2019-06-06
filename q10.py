##
## Imprima una tabla en formato CSV que contenga por cada clave 
## de la columna 5, la correspondiente cantidad de registros 
## asociados (filas en el archivo)
##
## aaa,13
## bbb,16
## ccc,23
## ddd,23
## eee,15
## fff,20
## ggg,13
## hhh,16
## iii,18
## jjj,18
##
##
import pandas
import datetime
df = pandas.read_csv('data.csv', sep='\t', encoding='latin-1', header=None, parse_dates=[2])
dfi=[]
dfi=df[[4]]
dic=[]
dic2=[]
for a in dfi[4]:
    b = a.split(',')
    for c in b:
        dic.append(c.split(':')[0])
        dic2.append(c.split(':')[-1])

lista = {'A': dic,
        'B': dic2
        }

df = pandas.DataFrame(lista,columns= ['A', 'B'])
df = df.groupby('A').count()
index = df.index
valores = df['B'].values
i=0
while i < 10:
    print(index[i] + ',' + str(valores[i]))
    i=i+1
