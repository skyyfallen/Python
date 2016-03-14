'''
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de se trabalho.
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (5o quilos) deve pagar uma multa
de R$4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e verifique se há excesso.
Se houver, gravar na variável excesso  na variável multa o valor da multa que João deverá pagar. Caso contrário mostrar tais variáveis com o coteúdo ZERO.
'''

peso = float(input('Digite o peso: '))
multa_kg = 4
if peso > 50:
    excesso = peso - 50
    multa = excesso * multa_kg
else:
    multa = excesso = 0
print ('Excesso: %.2fkg' %excesso)
print ('Multa: R$%.2f' %multa)




