'''
1) Faça um programa que peça dois números inteiros e imprima a soma desses dois números
'''

numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
print ('A soma dos dois números é %d' %(numero1 + numero2))




'''
2) Escreva um programa que leia um valor em metros e o exiba convertido em milímetros
'''

metros = float(input('Digite a quantidade de metros: '))
print ('%.1f metros equivale a %d milímetros' %(metros, metros*1000))




'''
3) Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.
'''

dias = int(input('Digite a quantidade de dias: '))
horas = int(input('Digite a quantidade de horas: '))
minutos = int(input('Digite a quantidade de minutos: '))
segundos = int(input('Digite a quantidade de segundos: '))
tempo = '%d segundos. ' %(((dias * 24 * 60) + (horas * 60) + minutos) * 60 + segundos)
print (tempo)




'''
4) Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. 
Exiba o valor do aumento e do novo salário.
'''

salario = float(input('Digite o salario: '))
porcentagem = float(input('Digite a porcentagem de aumento: '))
novoSalario = salario + (salario * porcentagem)/100
aumento = (salario * porcentagem)/100
print ('Novo salario: R$ %.2f ' %novoSalario)
print ('O aumento foi de %2.f reais ' %aumento)





'''
5) Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.
'''

preco = float(input('Digite o preço da mercadoria: '))
percentual = float(input('Digite o percentual de desconto: '))
desconto =(preco * percentual) / 100
novoPreco = preco = preco - (preco * percentual)/100

print ('O desconto foi de %.2f reais' %desconto)
print ('O novo preço é R$ %.2f' %novoPreco)




'''
6) Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem.
'''

distancia = float(input('Entre com a distância em km: '))
velocidade = float(input('Qual é a velocidade média esperada em km/h ? '))
tempo = distancia / velocidade
print ('O tempo aproximado é de %.2f horas' %tempo)




'''
7) Converta uma temperatura digitada em Celsius para Fahrenheit. F = 9*C/5 + 32
'''

c = float(input('Digite a temperatura em graus celsius: '))

f = 9*c/5 + 32
print('Essa quantidade de graus Celsius equivale a %.2f graus fahrenheit ' %f)




'''
8) Converta uma temperatura digitada em Fahrenheit para Celsius. F = 9*C/5 + 32
'''

f = float(input('Digite a temperatura em graus Fahrenheit: '))
c = (f - 32) * 5 / 9
print ('Essa quantidade de graus Fahrenheit equivale a %.2f graus Celsius' %c)




'''
9) Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias 
pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.
'''

km = int(input('Digite a quantidade de km percorridos: '))
dias = int(input('Digite a quantidade de dias de aluguel: '))
preco = (dias * 60) + (0.15 * km)
print(preco)




'''
10) Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros 
fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro, 
calcule quantos dias de vida um fumante perderá. Exiba o total de dias.
'''
cigarros = int(input('Digite a quantidade de cigarros fumados por dia: '))
anos = int(input('Digite a quantidade de anos que já fumou: '))
total_cigarros = anos * 365 * cigarros
dias_perdidos = total_cigarros / 144
print ('Você perdeu aproximadamente %.2f dias' %dias_perdidos)




'''
11) Sabendo que str( ) converte valores numéricos para string, calcule quantos dígitos há em 2 elevado a um milhão.
'''
print (len(str(2**1000000)))

