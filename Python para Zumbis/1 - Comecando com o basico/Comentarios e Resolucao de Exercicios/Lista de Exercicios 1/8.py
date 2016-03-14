'''
Converta uma temperatura digitada em Fahrenheit para Celsius. F = 9*C/5 + 32
'''

f = float(input('Digite a temperatura em graus Fahrenheit: '))
c = (f - 32) * 5 / 9
print ('Essa quantidade de graus Fahrenheit equivale a %.2f graus Celsius' %c)


