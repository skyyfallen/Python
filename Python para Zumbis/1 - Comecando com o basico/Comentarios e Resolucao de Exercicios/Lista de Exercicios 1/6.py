'''
Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem.
'''

distancia = float(input('Entre com a distância em km: '))
velocidade = float(input('Qual é a velocidade média esperada em km/h ? '))
tempo = distancia / velocidade
print ('O tempo aproximado é de %.2f horas' %tempo)


