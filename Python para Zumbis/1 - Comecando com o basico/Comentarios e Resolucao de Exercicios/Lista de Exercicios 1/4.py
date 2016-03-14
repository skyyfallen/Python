'''
Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. 
Exiba o valor do aumento e do novo salário.
'''

salario = float(input('Digite o salario: '))
porcentagem = float(input('Digite a porcentagem de aumento: '))
novoSalario = salario + (salario * porcentagem)/100
aumento = (salario * porcentagem)/100
print ('Novo salario: R$ %.2f ' %novoSalario)
print ('O aumento foi de %2.f reais ' %aumento)
