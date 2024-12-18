# Faca um programa que leia o sexo de uma pessoa, mas so aceita os valores 'M' Ou 'F'. Caso esteja errado, peca a digitacao novamente ate ter o valor correto.

print('\n {:=^45}'.format('\033[1m VALIDACAO DE DADOS! \033[m'))

sexo = str(input('Qual e o seu sexo [M/F]: ')).strip().upper()[0] #Caso digite Masculino ou Feminino, pega somente a primeira letra.

while sexo not in 'MF':
    sexo = str(input('\nINVALIDO! Por favor digite M ou F: ')).strip().upper()[0]

print('\n\033[33mObrigado! Seu genero foi cadastrado com sucesso no sistema!\033[m')
