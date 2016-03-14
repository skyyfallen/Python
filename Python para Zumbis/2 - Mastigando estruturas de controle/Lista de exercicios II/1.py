'''
Faça um programa que peça os três lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo.
Infique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
'''


lado1 = int(input('Digite o primeiro lado: '))
lado2 = int(input('Digite o segundo lado: '))
lado3 = int(input('Digite o terceiro lado: '))

if lado1 > lado2 + lado3 or lado2 > lado1 + lado3 or lado3 > lado1 + lado2:
    print ('Um dos lados está maior que a soma dos outros dois lados. Não pode ser um triângulo!')
elif lado1 == lado2 == lado3:
    print ('Triângulo equilátero')
elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
    print ('Triângulo isósceles')
else:
     print ('Triângulo escaleno')


