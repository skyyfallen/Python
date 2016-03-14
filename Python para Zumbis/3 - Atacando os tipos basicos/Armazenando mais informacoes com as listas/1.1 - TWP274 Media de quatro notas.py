#Faça um programa que leia quatro notas, mostre as notas e a média na tela

notas = []
i = 1
while i <= 4:
    nota = float(input('Digite a %d nota: ' %i))
    notas.append(nota)
    i += 1
soma = 0
i = 0
while i <= 3:
    soma += notas[i] 
    media = soma/4
    i += 1
print (notas)
print ('Media: %.2f' %media)
