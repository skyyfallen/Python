# Calcule o fatorial de um número inteiro n

i = 1
fatorial = 1
numero = int(input('Digite um número: '))
while i <= numero:
    fatorial = fatorial * i
    i = i + 1
print ('Fatorial(%d) = %d' %(numero, fatorial))
