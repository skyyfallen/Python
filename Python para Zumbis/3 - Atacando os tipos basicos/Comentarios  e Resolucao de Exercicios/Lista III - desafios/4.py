#Dado um número inteiro positivo, determine a sua decomposição em fatores primos calculando também a multiplicidade de cada fator.


numero = int(input('Digite um número: '))
for i in range(2, numero):
  while numero % i == 0:
    print (i)
    numero = numero / i
