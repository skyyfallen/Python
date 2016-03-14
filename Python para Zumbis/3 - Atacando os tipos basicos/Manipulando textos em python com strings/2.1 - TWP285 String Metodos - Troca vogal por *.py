#Faça um programa que leia uma palavra e troque as vogais por "*"

palavra = raw_input('Palavra: ')
i = 0
troca = ''
while i < len(palavra):
    if palavra[i] in 'aeiou':
        troca = troca + '*'
    else:
        troca = troca + palavra[i]
    i += 1
print (troca)
