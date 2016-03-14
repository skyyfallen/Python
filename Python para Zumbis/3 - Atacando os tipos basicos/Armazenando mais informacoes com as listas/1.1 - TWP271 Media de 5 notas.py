#Calcule a média de 5 notas

notas = [6, 5.5, 9, 7, 8]


soma = 0
i = 0
while i < 5:
    soma = soma + notas[i]
    i = i + 1
    media = soma / i
print ('Soma: %.2f' %soma)
print ('Media: %.2f' %media)
