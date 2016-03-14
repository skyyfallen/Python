#Faça um programa que peça um inteiro positivo e o mostre invertido. Ex.: 1234 gera 4321


numero = int(input('Número: '))
inverso = 0
while numero > 0:
  inverso *= 10
  inverso += numero % 10
  numero //= 10
  inv = inverso
print('O inverso é %d' %inv)
