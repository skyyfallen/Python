#Faça um programa que leia um vetor de 10 números reais e mostre-os na ordem inversa

vetor = []
i = 1
while i <= 10:
    numero = int(input('Número: '))
    vetor.append(numero)
    i += 1
print (vetor)
i = 9
while i >= 0:
    print (vetor[i])
    i -= 1
