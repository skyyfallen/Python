numero = int(input('Digite um número maior que 2: '))

i = 1

while i <= numero:
    if i % 2 == 0:
        print ('%d é par' %i)
    else:
        print ('%d é impar' %i)
    i = i + 1
