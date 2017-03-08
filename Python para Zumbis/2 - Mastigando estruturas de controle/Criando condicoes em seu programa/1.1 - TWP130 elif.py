'''
Considere a empresa de telefonia Tchau. Abaixo de 200 minutos, a empresa cobra R$ 0,20 por minuto.
Entre 200 e 400 minutos, o preço é de R$0,18. Acima de 400 minutos o preço por minuto é R$ 0,15.
Calcule sua conta de telefone.
'''

minutos = int(input('Quantidade de minutos: '))
if minutos < 200:
    preco = 0.20
elif minutos <= 400:
    preco = 0.18
elif minutos <= 800:
    preco = 0.15
else:
    preco = 0.08
print ('Conta: R$%.2f' %(minutos * preco))
    
