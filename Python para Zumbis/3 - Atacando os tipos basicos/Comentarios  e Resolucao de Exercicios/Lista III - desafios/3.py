#Verifique se um inteiro positivo n é primo.

numero = int(input('Digite um número: '))
i = 1
divisores = 0
while i <= numero:
  if numero % i == 0:
    divisores = divisores + 1
  i = i + 1
print (divisores == 2)



