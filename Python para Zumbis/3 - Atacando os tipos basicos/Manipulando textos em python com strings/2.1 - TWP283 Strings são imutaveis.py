#Existe uma biblioteca que permite string mutável, mas a string padrão não é imutável.

#Vai dar erro ao tentar fazer a troca do caracter na posição 0 por @.
'''
texto = 'Alô Mundo'
texto[0] = '@'
'''

#Essa troca pode ser feita usando a concatenação

texto = 'Alô Mundo'
texto = '@' + texto[1:]
print (texto)
