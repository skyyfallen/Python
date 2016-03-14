'''
Sorteie 20 inteiros entre 1 e 100 numa lista. Armazene os números pares na lista PAR e os
números ímpares na lista IMPAR. Imprima as três listas.
'''

import random

lista = []
par = []
impar = []
for i in range(20):
    numero = random.randint(1,100)
    lista.append(numero)
    if numero % 2 ==0:
        par.append(numero)
    else:
        impar.append(numero)
print ('Lista sorteada:')
print lista
par.sort()
impar.sort()
print "-"*78
print ('\nPar:')
print par
print ('\nImpar:')
print impar



