"""
Sorteie 10 inteiros entre 1 e 100 para uma lista e descubra o maior e o menor valor, sem usar 
as funções max e min. 
"""

import random

lista = []
maior = 0
menor = 100

for i in range(10):
	numero = random.randint(1,100)
	lista.append(numero)

	if numero < menor: 
		menor = numero
	if numero > maior:
		maior = numero
print ('Lista sorteada:')
print lista
lista.sort()
print "-"*40
print ('\nLista em ordem crescente:')
print lista
print("\nMenor número: %d - Maior número: %d" %(menor, maior))
print "-"*40
