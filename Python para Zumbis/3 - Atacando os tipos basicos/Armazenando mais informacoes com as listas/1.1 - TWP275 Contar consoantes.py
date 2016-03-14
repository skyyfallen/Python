#Faça um Programa que leia um vetor de 10 caracteres minúsculos e diga quantas consoantes foram lidas.

letras = []
i = 1
while i <= 10:
    letra = str(input('Letra: '))
    letras.append(letra)
    #letras.append(str(input('Letra: ')))
    i = i + 1

print (letras)
'''
i = 0
cont = 0
while i <= 9:
    if letras[i] not in 'aeiou':
        cont = cont + 1
    i = i + 1
print(cont)



'''
