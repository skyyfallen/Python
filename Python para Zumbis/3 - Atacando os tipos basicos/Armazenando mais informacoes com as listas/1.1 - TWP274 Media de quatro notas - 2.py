#Faça um programa que leia quatro notas, mostre as notas e a média na tela

notas = []
soma = 0
i = 1
while i <= 4:
    nota = float(input('Digite a %d nota: ' %i))
    notas.append(nota)
    soma += nota
    i += 1
    media = soma/4
print (notas)
print ('Media: %.2f' %media)
