'''
Indique como um troco deve ser dado utilizando-se um número mínimo de notas. Seu algoritmo deve ler o valor da conta a ser paga e o valor
do pagamento efetuado desprezando os centavos. Suponha que as notas para troco sejam as de 50, 20, 10, 5, 2 e 1 reais, e que nenhuma delas
esteja em falta no caixa.
'''

conta = float(input('Digite o valor da conta: R$'))
pagamento = float(input('Digite o pagamento: R$'))
notas = [50, 20, 10 ,5, 2, 1]
troco = pagamento - conta
print ('Troco: R$%.2f' %troco)
for nota in notas:
    while troco >= nota:
        print ('Uma nota de %d' %nota)
        troco -= nota

    


