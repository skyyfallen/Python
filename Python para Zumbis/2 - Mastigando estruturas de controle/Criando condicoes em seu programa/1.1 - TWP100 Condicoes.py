'''
Pergunte a velocidade de um carro, supondo um valor inteiro. Caso ultrapasse 110km/h, exiba uma mensagem dizendo que o usuário foi multado.
Neste caso, exiba o valor da multa, cobrando R$ 5,00 por km acima de 110
'''

velocidade = int(input('Digite a velocidade do carro: '))
if velocidade > 110:
    print('Você foi multado!')
    multa = 5 * (velocidade - 110)
    print ('Valor da multa %d reais' %multa)
if velocidade <= 110:
    print('Você não foi multado!')
