#Imprimir os números pares entre 0 e um número fornecido usando if

numero = int(input('Digite um número maior que 0: '))

i = 0

while i <= numero:
    if i % 2 == 0:
        print (i)
    i = i + 1
