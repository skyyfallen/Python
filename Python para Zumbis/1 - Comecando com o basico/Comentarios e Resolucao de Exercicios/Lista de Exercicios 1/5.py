'''
Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.
'''

preco = float(input('Digite o preço da mercadoria: '))
percentual = float(input('Digite o percentual de desconto: '))
desconto =(preco * percentual) / 100
novoPreco = preco = preco - (preco * percentual)/100

print ('O desconto foi de %.2f reais' %desconto)
print ('O novo preço é R$ %.2f' %novoPreco)
