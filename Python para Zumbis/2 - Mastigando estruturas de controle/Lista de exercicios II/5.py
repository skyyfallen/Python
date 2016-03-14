'''
Faça um Programa que leia três números e mostre o maior e o menor deles.
'''

numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
numero3 = int(input('Digite o terceiro número: '))

if numero1 >= numero2 and numero1 >= numero3:
    print ('O primeiro número: %d é maior' %numero1)
elif numero2 >= numero3:
    print ('O segundo número: %d é maior' %numero2)
else:
    print ('O terceiro número: %d é maior' %numero3)

if numero1 <= numero2 and numero1 <= numero3:
    print ('O primeiro número: %d é menor' %numero1)
elif numero2 <= numero3:
    print ('O segundo número: %d é menor' %numero2)
else:
    print ('O terceiro número: %d é menor' %numero3)
