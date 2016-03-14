#Cálcule a média de dez números inteiros

n = 1
soma = 0
while n <= 10:
    x = float(input('Digite o %d número: ' %n))
    soma = soma + x
    media = soma / n
    n = n + 1
print ('Soma: %.0f' %soma)
print ('Média: %.2f' %media)
