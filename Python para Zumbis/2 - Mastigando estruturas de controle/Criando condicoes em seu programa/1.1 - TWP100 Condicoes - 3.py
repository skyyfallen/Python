'''
Verificar se um carro é novo ou velho. Se o carro tiver pelom menos três anos é novo.
'''

idade = int(input('Digite a idade do carro: '))
if idade <= 3:
    print('Seu carro é novo!')
else:
    print('Ops! Seu carro é velho!')
