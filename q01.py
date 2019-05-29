##
## Imprima la suma de la segunda columna.
##
# Guarda cada linea del archivo como elemento de una lista
file = open('data.csv', 'r').readlines()

# Quitamos el ultimo caracter de cada elemento
file = [row[0:-1] for row in file]

# Separa los caracteres por tabulacion
file = [row.split('\t') for row in file]
data = file

suma_col = 0
for e in data:
    suma_col += int(e[1])
print(suma_col)