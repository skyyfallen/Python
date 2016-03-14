#Faça um programa que solicite a data de nascimento (dd/mm/aaaa) e imprima com o nome do mês por extenso.

#python 2.7
dia, mes, ano = raw_input('Data (dd/mm/aaaa): ').split('/')
meses = ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro', 'dezembro']
print ('%s de %s de %s' %(dia, meses[int(mes) -1], ano))

#python 3.4.0
dia, mes, ano = input('Data (dd/mm/aaaa): ').split('/')
meses = ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro', 'dezembro']
print ('%s de %s de %s' %(dia, meses[int(mes) -1], ano))

