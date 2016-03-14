'''
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
'''


#Sintaxe Python 2.7

usuario = raw_input('Nome: ')
senha = raw_input('Senha: ')
while senha == usuario:
    print ('A senha deve ser diferente do usuário!')
    usuario = raw_input('Usuário: ')
    senha = raw_input('Senha: ')
print ('Nome: %s' %usuario)
print ('Senha: %s' %senha)



'''
#Sintaxe Python 3

usuario = input('Nome: ')
senha = input('Senha: ')
while senha == usuario:
    print ('A senha deve ser diferente do usuário!')
    usuario = input('Usuário: ')
    senha = input('Senha: ')
print ('Nome: %s' %usuario)
print ('Senha: %s' %senha)
'''
