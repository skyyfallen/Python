#Dados dois números inteiros positivos, determinar o máximo divisor comum entre eles usando o algoritmo de Euclides.

numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))

while numero1 % numero2 != 0:
    numero1, numero2 = numero2, numero1%numero2
print ('mdc = %d' %numero2)
