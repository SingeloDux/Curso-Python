'''
Faca  um formulario que pergunte o nome, o NUIT, endereco, idade, altura e telefone e imprima em um relatorio organizado!
'''
print('=-=-=-=-=-=-= CADASTRO DE USUARIOS =-=-=-=-=-=-=')
nome = str(input('Digite o nome: ')).strip()
idade = int(input('Digite a idade: '))
telefone = str(input('Digite o telefone: ')).strip()
nuit = int(input('Digite o NUIT: '))
adress = str(input('DIgite o endereco: ')).strip()

print('\n=-=-=-=-=-=-= DADOS DO USUARIO =-=-=-=-=-=-=')

print('NOME \t IDADE \t TELEFONE \t NUIT \t ENDERECO')
print(nome, ' ', idade,'  ', telefone,'  ', nuit,'  ', adress)
