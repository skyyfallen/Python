'''
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
que custam R$ 80,00. Informe ao usuário a quantidade de latas de tinta a serem compradas e o preço total.
Obs.:somente são vendidos umnúmero inteiro de latas.
'''

metros = float(input('Digite a quantidade de metros quadrados da área a ser pintada: '))
if metros % 54 == 0:
    latas = metros / 54 
else:
    latas = int(metros / 54) + 1

preco = latas * 80
print ('Você vai  precisar de %d lata(s) de tinta a um custo de R$%.2f.' %(latas, preco))
